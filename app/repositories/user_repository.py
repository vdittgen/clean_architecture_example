from abc import ABC, abstractmethod
from typing import Optional
# from sqlalchemy.orm import Session

from app.domain.user import IUser  # , User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: IUser) -> None:
        pass

    @abstractmethod
    def update(self, user: IUser) -> None:
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


class InMemoryUserRepository(IUserRepository):
    def __init__(self):
        self._users = {}
        self._last_id = 0

    def save(self, user: IUser) -> None:
        if user.id is None:
            self._last_id += 1
            user.set_id(self._last_id)
        self._users[user.id] = user

    def update(self, user: IUser) -> None:
        if user.id not in self._users:
            raise ValueError(f"User with ID {user.id} does not exist")
        self._users[user.id] = user

    def delete(self, user_id: int) -> None:
        if user_id not in self._users:
            raise ValueError(f"User with ID {user_id} does not exist")
        del self._users[user_id]

    def get_by_id(self, user_id: int) -> Optional[IUser]:
        return self._users.get(user_id)

    def get_by_email(self, email: str) -> Optional[IUser]:
        for user in self._users.values():
            if user.email == email:
                return user
        return None


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
