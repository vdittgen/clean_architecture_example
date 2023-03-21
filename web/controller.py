from flask import Flask
from views import views_bp


def create_app():
    web_app = Flask(__name__)
    web_app.register_blueprint(views_bp)
    return web_app


web_app = create_app()

if __name__ == "__main__":
    web_app.run()
