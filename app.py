
from flask import Flask
from flask_migrate import Migrate
from config import Config
from models import db
from routes import chat_bp, messages_bp

from prometheus_flask_exporter import PrometheusMetrics

# Initialize extensions outside the factory to allow extension objects to be reused.
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask-SQLAlchemy and Migrate with the app instance
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(chat_bp)
    app.register_blueprint(messages_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    metrics = PrometheusMetrics(app)
    with app.app_context():
        db.create_all()  # Optional, depending on your setup
    app.run(debug=True)