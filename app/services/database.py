from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.repositories.user_repository import IUserRepository, \
    UserSqlAlchemyRepository


class DatabaseService:
    def __init__(self, db_uri: str):
        self.engine = create_engine(db_uri)
        self.Session = sessionmaker(bind=self.engine)

    def get_user_repository(self) -> IUserRepository:
        return UserSqlAlchemyRepository(self.Session())
