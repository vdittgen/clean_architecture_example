from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from app.domain.user import IUser
from app.repositories.user_repository import IUserRepository


class IGetUsers(ABC):
    @abstractmethod
    def execute(self) -> IUser:
        pass


class GetUsers(IGetUsers):
    def __init__(self, user_repo: IUserRepository):
        self._user_repo = user_repo

    def execute(self) -> List[IUser]:
        users = self._user_repo.get_users()
        return users
