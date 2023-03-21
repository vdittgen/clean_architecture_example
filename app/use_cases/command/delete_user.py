from __future__ import annotations
from abc import ABC, abstractmethod

from app.domain.user import IUser
from app.repositories.user_repository import IUserRepository


class IDeleteUser(ABC):
    @abstractmethod
    def execute(
        self,
        email: str
    ) -> IUser:
        pass


class DeleteUser(IDeleteUser):
    def __init__(self,
                 user_repo: IUserRepository
                 ):
        self._user_repo = user_repo

    def execute(
        self,
        email: int
    ):
        self._user_repo.delete(email)

        return
