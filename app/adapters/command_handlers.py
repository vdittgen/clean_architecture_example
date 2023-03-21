from typing import List
from app.repositories.user_repository import IUserRepository, IUser
from app.services.email import IEmailService
from app.use_cases.command.delete_user import DeleteUser
from app.use_cases.command.register_user import RegisterUser
from app.use_cases.query.get_user import GetUser
from app.use_cases.query.get_users import GetUsers


class RegisterUserHandler:
    def __init__(self,
                 user_repo: IUserRepository,
                 email_service: IEmailService):
        self._register_user = RegisterUser(user_repo, email_service)

    def __call__(
        self, username: str, email: str, password: str, role: str = None
    ) -> IUser:
        return self._register_user.execute(username, email, password, role)


class GetUserHandler:
    def __init__(self, user_repo: IUserRepository):
        self._get_user = GetUser(user_repo)

    def __call__(self, email: str) -> IUser:
        return self._get_user.execute(email)


class GetUsersHandler:
    def __init__(self, user_repo: IUserRepository):
        self._get_users = GetUsers(user_repo)

    def execute(self) -> List[IUser]:
        return self._get_users.execute()


class DeleteUserHandler:
    def __init__(self, user_repo: IUserRepository):
        self._delete_user = DeleteUser(user_repo)

    def __call__(self, email: str) -> IUser:
        return self._delete_user.execute(email)
