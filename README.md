# 🚘 Vehicle Dashboard – Kubernetes (Minikube Deployment)

This project demonstrates a **full-stack vehicle telematics system** deployed on **Kubernetes (Minikube)**.  
It represents a realistic **IoT + DevOps** setup where vehicle telemetry is collected, processed, stored, and visualized through containerized microservices.

---

## 🧠 Concept Overview

The system simulates an IoT pipeline:

1. **IoT Publisher (Local)** – Sends vehicle telemetry data over MQTT.  
2. **Backend Subscriber (Flask)** – Runs inside Kubernetes, receives data, and stores it in MySQL.  
3. **MySQL Database** – Stores all telemetry logs.  
4. **Frontend (React)** – Displays real-time vehicle stats and system data visually.

All components run as containers in a **single Kubernetes cluster** (Minikube in this case).

---

## 🧱 Kubernetes Architecture

| Component | Description | Type |
|------------|-------------|------|
| **React Dashboard** | Frontend for data visualization | NodePort Service |
| **Flask Backend Subscriber** | Handles MQTT data & writes to MySQL | ClusterIP Service |
| **MySQL Database** | Stores all telemetry logs | Headless ClusterIP |
| **ConfigMap** | Holds environment variables (DB details, backend URL) | Configuration |
| **Secret** | Stores database credentials | Secret Object |

---

## 📁 Directory Structure

```
my_first_vehicle_dashboard/
│
├── k8s/
│   ├── frontend-deployment.yml
│   ├── frontend-service.yml
│   ├── backend-deployment.yml
│   ├── backend-service.yml
│   ├── mysql-deployment.yml
│   ├── mysql-service.yml
│   ├── mysql-secret.yml
│   ├── app-configmap.yml
│
└── Docs/
    ├── Docker_and_Kubernetes_Command_CheatSheet.pdf
    ├── EC2_Docker_Compose_Infrastructure.pdf
    └── README.md
```

---

## ⚙️ Setup & Deployment

### 1️⃣ Start Minikube
```bash
minikube start
```

### 2️⃣ Deploy All Components
```bash
kubectl apply -f k8s/
```

### 3️⃣ Verify Deployments
```bash
kubectl get pods
kubectl get svc
```

Example output:
```
NAME                                  READY   STATUS    RESTARTS   AGE
backend-subscriber-6bfcd59d76-gjnd9   1/1     Running   0          23m
mysql-5b69d4dd8-hjfjk                 1/1     Running   0          23m
react-dashboard-6755b4777-fgk24       1/1     Running   0          23m
```

### 4️⃣ Access the Frontend
```bash
minikube service frontend-service --url
```

Example:
```
http://192.168.49.2:32141
```

---

## 🧩 Data Flow

1. **MQTT Publisher** sends JSON payloads like:
   ```json
   {
     "vehicle_ID": "Angad001",
     "Speed": 70,
     "Battery_voltage": 13.98,
     "Engine_Temp": 101,
     "Fuel_Level": 64,
     "timestamp": "2025-11-03 16:02:28",
     "location": "18.480248, 74.021696"
   }
   ```

2. **Backend Subscriber** inserts data into MySQL:
   ```sql
   INSERT INTO vehicle_logs 
   (vehicle_ID, Speed, Battery_voltage, Engine_Temp, Fuel_Level, timestamp, location)
   VALUES (...);
   ```

3. **Frontend (React)** reads backend API responses and visualizes telemetry in charts and tables.

---

## 🧾 Sample Database Entries

| id | vehicle_ID | Speed | Battery_voltage | Engine_Temp | Fuel_Level | timestamp | location |
|----|-------------|--------|-----------------|--------------|-------------|------------|-----------|
| 1 | Angad001 | 118 | 11.03 | 105 | 15 | 2025-11-03 16:02:08 | 18.480248, 74.021696 |
| 2 | Angad001 | 47 | 11.06 | 100 | 67 | 2025-11-03 16:02:18 | 18.480248, 74.021696 |

---

## 🧠 DevOps Concepts Covered

- **Docker**: Containerized frontend, backend, and database  
- **Kubernetes**: Pod orchestration and service management  
- **ConfigMap & Secrets**: Centralized environment configuration  
- **Networking**: Service discovery between backend, frontend, and database  
- **Database Connectivity**: Persistent data layer inside cluster  
- **Cluster Monitoring**: Using `kubectl` commands and logs

---

## 🌩️ Next Steps (Production-Grade Upgrade)

| Area | Upgrade |
|------|----------|
| **Cluster** | Move from Minikube → AWS **EKS** |
| **Infra as Code** | Automate with **Terraform** |
| **CI/CD** | Integrate with **Jenkins** or **GitHub Actions** |
| **Monitoring** | Add **Grafana + Prometheus** |
| **Ingress** | Use NGINX Ingress Controller for HTTPS routing |
| **Storage** | Add Persistent Volume Claims (PVCs) for MySQL |

---

## 🌿 Git Branching Strategy

| Branch | Description |
|--------|--------------|
| `feature/devops-architecture-setup` | Base DevOps setup for EC2, Jenkins, and Docker |
| `feature/docker-compose-aws` | AWS EC2 deployment using Docker Compose |
| `feature/k8s` | Kubernetes (Minikube/EKS) deployment with ConfigMaps, Secrets, and Pods |

---

## 📚 References

- [`Docs/Docker_and_Kubernetes_Command_CheatSheet.pdf`](./Docs/Docker_and_Kubernetes_Command_CheatSheet.pdf)  
- [`Docs/EC2_Docker_Compose_Infrastructure.pdf`](./Docs/EC2_Docker_Compose_Infrastructure.pdf)

---

## 🧑‍💻 Author

**Angad B.**  
Cloud, IoT & DevOps Engineer  
📍 Pune, India  
🚀 Passionate about building cloud-native IoT and DevOps ecosystems
