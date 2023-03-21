from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from app.repositories.user_repository import IUserRepository, \
    InMemoryUserRepository
from app.adapters.command_handlers import RegisterUserHandler, GetUserHandler
from app.services.email import IEmailService, MockEmailService
from app.use_cases.command.register_user import UserAlreadyExistsError


api_app = FastAPI()
user_repo: IUserRepository = InMemoryUserRepository()
email_service: IEmailService = MockEmailService()
register_user_handler = RegisterUserHandler(user_repo, email_service)
get_user_handler = GetUserHandler(user_repo)


class UserIn(BaseModel):
    username: str
    email: str
    password: str
    role: Optional[str] = None


class EmailIn(BaseModel):
    email: str


class UserOut(BaseModel):
    username: str
    email: str
    is_active: bool
    role: Optional[str] = None


@api_app.post("/users", response_model=UserOut)
async def register_user(user_in: UserIn):
    try:
        user = register_user_handler(user_in.username, user_in.email,
                                     user_in.password, user_in.role)
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e))
    return UserOut(
        username=user.username,
        email=user.email,
        is_active=user.is_active,
        role=user.role,
    )


@api_app.post("/users/get")
async def get_user(email_in: EmailIn):
    if email_in.email is None:
        raise HTTPException(status_code=400, detail="Missing email")

    user = get_user_handler(email_in.email)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserOut(
        username=user.username,
        email=user.email,
        is_active=user.is_active,
        role=user.role,
    )
