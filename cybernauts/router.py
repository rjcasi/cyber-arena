from flask import Blueprint, render_template

cybernauts_bp = Blueprint(
    "cybernauts",
    __name__,
    template_folder="../templates/cybernauts"
)

@cybernauts_bp.route("/")
def cockpit():
    return render_template("cybernauts/cockpit.html")
