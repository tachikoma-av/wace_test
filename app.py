from flask import Flask
from flask_migrate import Migrate
from config import Config
from prometheus_flask_exporter import PrometheusMetrics

from models import db
from routes import chat_bp, messages_bp



# Initialize extensions
migrate = Migrate()
app = Flask(__name__)
app.config.from_object(Config)

metrics = PrometheusMetrics(app)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(chat_bp)
app.register_blueprint(messages_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure the database is created
    app.run(debug=True)