#!/bin/bash
# ================================================
# 🚗 Vehicle Dashboard - Kubernetes Launch Script
# -----------------------------------------------
# This script deploys MySQL, Backend, and Frontend
# pods + services in Minikube or Kubernetes.
# ================================================

echo "🚀 Starting Vehicle Dashboard Deployment..."

# Step 1: Apply Configurations
echo "⚙️  Applying ConfigMaps and Secrets..."
kubectl apply -f k8s/config/vehicle-config.yml
kubectl apply -f k8s/config/vehicle-secrets.yml

# Step 2: Deploy MySQL Pod and Service
echo "🗄️  Deploying MySQL Pod and Service..."
kubectl apply -f k8s/pods/mysql-pod.yml
kubectl apply -f k8s/services/mysql-service.yml

# Wait for MySQL to be ready
echo "⏳ Waiting for MySQL pod to initialize..."
kubectl wait --for=condition=Ready pod/mysql-db --timeout=90s

# Step 3: Deploy Backend Pod and Service
echo "⚙️  Deploying Backend (Flask Subscriber)..."
kubectl apply -f k8s/pods/backend-pod.yml
kubectl apply -f k8s/services/backend-service.yml

# Wait for backend to be ready
kubectl wait --for=condition=Ready pod/backend-subscriber --timeout=90s

# Step 4: Deploy Frontend Pod and Service
echo "🖥️  Deploying React Dashboard..."
kubectl apply -f k8s/pods/frontend-pod.yml
kubectl apply -f k8s/services/frontend-service.yml

# Wait for frontend to be ready
kubectl wait --for=condition=Ready pod/react-dashboard --timeout=90s

# Step 5: Show summary
echo "✅ Deployment completed successfully!"
echo
kubectl get pods
kubectl get svc
echo
echo "🌐 Access your dashboard at: http://$(minikube ip):30080"
echo "--------------------------------------------------------"
