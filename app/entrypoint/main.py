# main.py
from flask import Flask
from adapters.web.views import views_bp

app = Flask(__name__)
app.register_blueprint(views_bp)
