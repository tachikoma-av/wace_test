#!/bin/sh

echo "Waiting for PostgreSQL to start..."
while ! nc -z db 5432; do sleep 1; done  # Ожидаем, пока PostgreSQL запустится

echo "Initializing database migrations..."
if [ ! -d "migrations" ]; then
    flask db init
fi
flask db migrate -m "Initial migration"
flask db upgrade

echo "Starting Flask app..."
exec flask run --host=0.0.0.0
