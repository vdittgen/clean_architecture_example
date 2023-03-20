from __future__ import annotations
from abc import ABC, abstractmethod

from app.domain.user import IUser
from app.repositories.user_repository import IUserRepository


class IGetUser(ABC):
    @abstractmethod
    def execute(
        self,
        email
    ) -> IUser:
        pass


class GetUser(IGetUser):
    def __init__(self, user_repo: IUserRepository):
        self._user_repo = user_repo

    def execute(
        self,
        email: str
    ) -> IUser:
        user = self._user_repo.get_by_email(email)
        return user
