# adapters/web/views.py
from flask import Blueprint, render_template

views_bp = Blueprint("views", __name__, template_folder="templates")


@views_bp.route("/")
def index():
    message = "Hello, World!"
    return render_template("index.html", message=message)
