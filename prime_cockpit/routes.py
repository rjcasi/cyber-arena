from flask import Blueprint, render_template
from .telemetry import (
    get_organ_status,
    get_cybernaut_memory,
    get_activity_feed,
    get_heartbeat
)

prime_bp = Blueprint(
    "prime",
    __name__,
    template_folder="../templates/prime_cockpit"
)

@prime_bp.route("/")
def dashboard():
    return render_template(
        "prime_cockpit/dashboard.html",
        organ_status=get_organ_status(),
        memory=get_cybernaut_memory(),
        activity=get_activity_feed(),
        heartbeat=get_heartbeat()
    )

@prime_bp.route("/status")
def status():
    return {
        "heartbeat": get_heartbeat(),
        "organ_status": get_organ_status(),
        "memory": get_cybernaut_memory(),
        "activity": get_activity_feed()
    }
