#!/bin/sh

echo "Waiting for PostgreSQL to start..."
while ! timeout 1 bash -c 'echo > /dev/tcp/db/5432'; do sleep 1; done

echo "Initializing database migrations..."
if [ ! -d "migrations" ]; then
    flask db init
fi
flask db migrate -m "Initial migration"
flask db upgrade

echo "Starting Flask app..."
exec flask run --host=0.0.0.0
