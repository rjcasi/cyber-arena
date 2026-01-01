from flask import Blueprint, render_template, request
from .core import process_math

math_engine_bp = Blueprint(
    "math_engine",
    __name__,
    template_folder="../templates/math_engine"
)

@math_engine_bp.route("/")
def dashboard():
    return render_template("math_engine/dashboard.html")

@math_engine_bp.route("/compute", methods=["POST"])
def compute():
    query = request.form.get("query", "")
    result = process_math(query)
    return render_template("math_engine/dashboard.html", query=query, result=result)
