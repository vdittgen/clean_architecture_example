from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional


class IUser(ABC):
    @abstractmethod
    def __init__(
        self,
        id: Optional[int],
        username: str,
        email: str,
        password: str,
        is_active: bool,
        role: Optional[str],
    ) -> None:
        pass

    @property
    @abstractmethod
    def id(self) -> Optional[int]:
        pass

    @property
    @abstractmethod
    def username(self) -> str:
        pass

    @property
    @abstractmethod
    def email(self) -> str:
        pass

    @property
    @abstractmethod
    def password(self) -> str:
        pass

    @property
    @abstractmethod
    def is_active(self) -> bool:
        pass

    @property
    @abstractmethod
    def role(self) -> Optional[str]:
        pass

    @abstractmethod
    def activate(self) -> None:
        pass

    @abstractmethod
    def set_id(self, id: int) -> None:
        pass

    @abstractmethod
    def deactivate(self) -> None:
        pass

    @abstractmethod
    def change_password(self, new_password: str) -> None:
        pass


class User(IUser):
    def __init__(
        self,
        id: Optional[int],
        username: str,
        email: str,
        password: str,
        is_active: bool,
        role: Optional[str],
    ) -> None:
        self._id = id
        self._username = username
        self._email = email
        self._password = password
        self._is_active = is_active
        self._role = role

    @property
    def id(self) -> Optional[int]:
        return self._id

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def password(self) -> str:
        return self._password

    @property
    def is_active(self) -> bool:
        return self._is_active

    @property
    def role(self) -> Optional[str]:
        return self._role

    def activate(self) -> None:
        self._is_active = True

    def deactivate(self) -> None:
        self._is_active = False

    def set_id(self, id: int) -> None:
        self._id = id

    def change_password(self, new_password: str) -> None:
        self._password = new_password
