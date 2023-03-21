from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

from app.domain.user import IUser, User
from app.repositories.user_repository import IUserRepository
from app.services.email import IEmailService


class UserAlreadyExistsError(Exception):
    pass


class IRegisterUser(ABC):
    @abstractmethod
    def execute(
        self,
        username: str,
        email: str,
        password: str,
        role: Optional[str] = None
    ) -> IUser:
        pass


class RegisterUser(IRegisterUser):
    def __init__(self,
                 user_repo: IUserRepository,
                 email_service: IEmailService
                 ):
        self._user_repo = user_repo
        self._email_service = email_service

    def execute(
        self,
        username: str,
        email: str,
        password: str,
        role: Optional[str] = None
    ) -> IUser:
        if self._user_repo.get_by_email(email) is not None:
            raise UserAlreadyExistsError(
                f"User with email {email} already exists")

        user = User(
            username=username,
            email=email,
            password=password,
            is_active=False,
            role=role,
        )
        self._user_repo.save(user)

        activation_link = f"https://example.com/activate/{user.email}"
        activation_message = f"Hello, {username}! Please activate your \
            account by clicking the following link: {activation_link}"
        self._email_service.send_activation_email(email, activation_message)

        return user
