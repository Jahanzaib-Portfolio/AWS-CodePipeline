#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
echo "Pulling image..."
docker pull jahanzaibkhan/simple-python-flask-app

# Run the Docker image as a container
echo "Running image as container..."
docker run -d -p 5000:5000 jahanzaibkhan/simple-python-flask-app
