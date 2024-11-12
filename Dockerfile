# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app to be accessible externally
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=backend/app.py
ENV FLASK_ENV=development

# Run Flask app
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]