from flask import Flask

# --- Organs ---
from organs.red_team.routes import red_team_bp
from organs.blue_team.routes import blue_team_bp
from organs.grey_team.routes import grey_team_bp

# --- Cybernauts ---
from cybernauts.router import cybernauts_bp

# --- Math Engine ---
from math_engine.routes import math_engine_bp

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(red_team_bp, url_prefix="/red")
app.register_blueprint(blue_team_bp, url_prefix="/blue")
app.register_blueprint(grey_team_bp, url_prefix="/grey")
app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")
app.register_blueprint(math_engine_bp, url_prefix="/math")

@app.route("/")
def index():
    return """
    <h1>CyberArena</h1>
    <p>Select a module:</p>
    <ul>
        <li><a href='/red'>Red Team</a></li>
        <li><a href='/blue'>Blue Team</a></li>
        <li><a href='/grey'>Grey Team</a></li>
        <li><a href='/cybernauts'>Cybernaut Cockpit</a></li>
        <li><a href='/math'>Math Engine</a></li>
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
