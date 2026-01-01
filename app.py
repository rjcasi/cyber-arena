from flask import Flask, render_template

# Import blueprints
from organs.red_team.routes import red_team_bp
from organs.blue_team.routes import blue_team_bp
from organs.grey_team.routes import grey_team_bp
from cybernauts.router import cybernauts_bp

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(red_team_bp, url_prefix="/red")
    app.register_blueprint(blue_team_bp, url_prefix="/blue")
    app.register_blueprint(grey_team_bp, url_prefix="/grey")
    app.register_blueprint(cybernauts_bp, url_prefix="/cybernauts")

    @app.route("/")
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
