#!/bin/bash

# --- Configuration ---
DOCKER_USER="angad696"
IMAGE_NAME="react-dashboard"
TAG="latest"
COMPOSE_FILE="docker-compose.prod.yml"

# --- Main Script ---
echo "------------------------------------------"
echo "🚀 React Dashboard Redeploy Script Started"
echo "------------------------------------------"

# 1. Get new EC2 Public IP
read -p "Enter the NEW EC2 Public IP Address (e.g., 13.233.120.45): " NEW_IP

if [ -z "$NEW_IP" ]; then
    echo "❌ Error: IP address cannot be empty. Exiting."
    exit 1
fi

NEW_URL="http://${NEW_IP}:5000"
echo "✅ New Backend URL set to: $NEW_URL"

# 2. Update .env file
echo "⚙️ Updating .env file with new backend URL..."
if grep -q "^REACT_APP_BACKEND_URL=" .env; then
    sed -i "s|^REACT_APP_BACKEND_URL=.*|REACT_APP_BACKEND_URL=$NEW_URL|" .env
else
    echo "REACT_APP_BACKEND_URL=$NEW_URL" >> .env
fi
echo "✅ .env updated successfully."

# 3. Build Docker image
echo "🏗️ Building new Docker image: $DOCKER_USER/$IMAGE_NAME:$TAG"
docker build -t $DOCKER_USER/$IMAGE_NAME:$TAG .

if [ $? -ne 0 ]; then
    echo "❌ Docker build failed. Exiting."
    exit 1
fi

# 4. Push to Docker Hub
echo "⬆️ Pushing image to Docker Hub..."
docker push $DOCKER_USER/$IMAGE_NAME:$TAG

if [ $? -ne 0 ]; then
    echo "❌ Docker push failed. Check login or repository name."
    exit 1
fi

# 5. Deploy using docker-compose
echo "🔄 Redeploying container with Docker Compose..."
docker compose -f $COMPOSE_FILE pull $IMAGE_NAME
docker compose -f $COMPOSE_FILE up -d $IMAGE_NAME

if [ $? -ne 0 ]; then
    echo "❌ Docker Compose deployment failed."
    exit 1
fi

echo "✅ Deployment complete!"
echo "🌐 Access your dashboard at: http://${NEW_IP}:3000"
echo "------------------------------------------"
