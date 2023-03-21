from werkzeug.exceptions import Conflict
from flask import Blueprint, render_template, request

from app.adapters.command_handlers import GetUsersHandler, \
    RegisterUserHandler, DeleteUserHandler
from app.repositories.user_repository import IUserRepository, \
    InMemoryUserRepository
from app.services.email import IEmailService, MockEmailService
from app.use_cases.command.register_user import UserAlreadyExistsError

users_blueprint = Blueprint('users', __name__)
user_repo: IUserRepository = InMemoryUserRepository()
email_service: IEmailService = MockEmailService()
register_user_handler = RegisterUserHandler(user_repo, email_service)
get_users_handler = GetUsersHandler(user_repo)
delete_user_handler = DeleteUserHandler(user_repo)
users = []


@users_blueprint.route('/', methods=['GET', 'POST'])
def index():
    users = []
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        try:
            register_user_handler(name, email, password, role)
            users = get_users_handler.execute()
        except UserAlreadyExistsError:
            raise Conflict("A user with the same email already exists")

    return render_template('index.html', users=users)


@users_blueprint.route('/delete/<string:email>', methods=['POST'])
def delete_user(email):
    try:
        delete_user_handler(email)
        users = get_users_handler.execute()
    except Exception as e:
        raise e

    return render_template('index.html', users=users)
