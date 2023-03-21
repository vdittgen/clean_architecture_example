from unittest.mock import Mock

from app.repositories.user_repository import IUserRepository, \
    InMemoryUserRepository
from app.services.email import IEmailService, MockEmailService
from app.use_cases.command.register_user import RegisterUser, \
    UserAlreadyExistsError
import pytest


@pytest.fixture
def mock_user():
    user = {"name": "test",
            "email": "john@a.com",
            "password": "123",
            "role": "admin"}
    return user


@pytest.fixture
def mock_register():
    user_repo: IUserRepository = InMemoryUserRepository()
    email_service: IEmailService = MockEmailService()
    register_user = RegisterUser(user_repo, email_service)
    return register_user


@pytest.fixture
def mock_register_error():
    user_repo: IUserRepository = InMemoryUserRepository()
    email_service: IEmailService = MockEmailService()
    register_user = RegisterUser(user_repo, email_service)
    register_user.execute = Mock()
    register_user.execute.side_effect = UserAlreadyExistsError

    return register_user


def test_transformer_transform(mock_register, mock_user):
    user = mock_register.execute(mock_user["name"],
                                 mock_user["email"],
                                 mock_user["password"],
                                 mock_user["role"])

    assert user._username == mock_user["name"]


def test_transformation_error(mock_register_error, mock_user):
    with pytest.raises(UserAlreadyExistsError):
        mock_register_error.execute(mock_user)
