import os

class Config:
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///chat.db")  # Using SQLite for simplicity
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@db:5432/plumber_assistant_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

