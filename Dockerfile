# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set environment variables to avoid interactive prompts during package installation
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=app.py

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
