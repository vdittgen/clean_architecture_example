from abc import ABC, abstractmethod
from typing import List, Optional
# from sqlalchemy.orm import Session

from app.domain.user import IUser  # , User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: IUser) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[IUser]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[IUser]:
        pass

    @abstractmethod
    def get_users(self) -> Optional[List[IUser]]:
        pass


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._users = {}
        self._last_id = 0

    def save(self, user: IUser) -> None:
        self._last_id += 1
        self._users[self._last_id] = user

    def delete(self, email: str) -> None:
        users_copy = self._users.copy()
        for key, user in users_copy.items():
            if user.email == email:
                del self._users[key]
                return
        raise ValueError(f"User with email {email} does not exist")

    def get_by_id(self, user_id: int) -> Optional[IUser]:
        return self._users.get(user_id)

    def get_by_email(self, email: str) -> Optional[IUser]:
        for user in self._users.values():
            if user.email == email:
                return user
        return None

    def get_users(self) -> Optional[List[IUser]]:
        return self._users.values()


"""
class UserSqlAlchemyRepository(IUserRepository):
    def __init__(self, session: Session):
        self.session = session

    def save(self, user: IUser) -> None:
        user_model = self._to_model(user)
        self.session.add(user_model)
        self.session.commit()
        user.id = user_model.id

    def update(self, user: IUser) -> None:
        user_model = self._to_model(user)
        self.session.merge(user_model)
        self.session.commit()

    def delete(self, user_id: int) -> None:
        self.session.query(UserModel).filter_by(id=user_id).delete()
        self.session.commit()

    def get_by_id(self, user_id: int) -> Optional[IUser]:
        user_model = self.session.query(UserModel) \
                .filter_by(id=user_id).first()
        return self._to_domain(user_model)

    def get_by_email(self, email: str) -> Optional[IUser]:
        user_model = self.session.query(UserModel) \
            .filter_by(email=email).first()
        return self._to_domain(user_model)

    def _to_model(self, user: IUser) -> UserModel:
        return UserModel(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            is_active=user.is_active,
            role=user.role,
        )

    def _to_domain(self, user_model: UserModel) -> Optional[IUser]:
        if user_model is None:
            return None
        return User(
            id=user_model.id,
            username=user_model.username,
            email=user_model.email,
            password=user_model.password,
            is_active=user_model.is_active,
            role=user_model.role,
        )
 """
