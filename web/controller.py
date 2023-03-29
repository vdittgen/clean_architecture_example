from flask import Flask
from web.views import users_blueprint


def create_app():
    web_app = Flask(__name__)
    web_app.register_blueprint(users_blueprint)

    return web_app


web_app = create_app()

if __name__ == "__main__":
    web_app.run(debug=True)
