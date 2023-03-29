from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)
    role = Column(String(20), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
