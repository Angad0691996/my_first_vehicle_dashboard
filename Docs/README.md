# 🚗 Vehicle Dashboard - Docker Compose on AWS EC2

A full-stack **IoT Vehicle Dashboard** deployed on an **AWS EC2 (t2.medium)** instance using **Docker Compose**.  
It integrates **Flask**, **React**, and **MySQL** containers to display live telemetry data from an MQTT-based vehicle publisher.

---

## ⚙️ Overview

| Component | Description | Port |
|------------|--------------|------|
| **MySQL (Database)** | Stores live vehicle telemetry data | 3307 |
| **Flask Backend (Subscriber)** | Receives MQTT messages and exposes `/latest` and `/api/logs` APIs | 5000 |
| **React Frontend (Dashboard)** | Visualizes live vehicle data from the backend | 3000 |

---

## 🧩 EC2 Configuration

| Parameter | Value |
|------------|--------|
| **AMI** | Canonical Ubuntu 24.04 (ami-02d26659fd82cf299) |
| **Instance Type** | t2.medium |
| **Storage** | 10 GiB |
| **Security Group** | Ports 22 (SSH), 3000 (React), 5000 (Flask), 3307 (MySQL) open |

---

## 🗂️ Project Structure

```
my_first_vehicle_dashboard/
├── backend/                     # Flask MQTT Subscriber
├── src/                         # React Frontend
├── Docs/
│   ├── EC2_Docker_Compose_Infrastructure.md
│   └── EC2_Docker_Compose_Infrastructure.pdf
├── assets/
│   ├── AWS_VM.png
│   ├── AWS-dashboard-1.png
│   ├── AWS-dashboard-2.png
│   └── AWS-dashboard-3.png
├── docker-compose.prod.yml      # Docker Compose configuration
├── .env                         # Environment variables
└── README.md
```

---

## 🐳 Docker Containers on EC2

```bash
$ docker ps
CONTAINER ID   IMAGE                                COMMAND                  STATUS          PORTS
99f378786ded   angad696/react-dashboard:latest      "/docker-entrypoint.…"   Up 14 mins      0.0.0.0:3000->80/tcp
3964b47e2c96   angad696/backend-subscriber:latest   "python subscriber.py"   Up 36 mins      0.0.0.0:5000->5000/tcp
dba706bcfd63   mysql:8.0                            "docker-entrypoint.s…"   Up 36 mins      0.0.0.0:3307->3306/tcp
```

---

## 🌍 Access Points

| Component | URL |
|------------|------|
| **React Dashboard** | [http://<EC2_PUBLIC_IP>:3000](http://<EC2_PUBLIC_IP>:3000) |
| **Flask Backend API** | [http://<EC2_PUBLIC_IP>:5000/latest](http://<EC2_PUBLIC_IP>:5000/latest) |

---

## 📸 Screenshots

### 🖥️ AWS VM & Dashboard View

| AWS VM | Dashboard |
|--------|------------|
| ![AWS VM](../assets/AWS_VM.png) | ![Dashboard](../assets/AWS-dashboard-1.png) |

### 📊 Additional Views
![Dashboard 2](../assets/AWS-dashboard-2.png)
![Dashboard 3](../assets/AWS-dashboard-3.png)

---

## 🧰 How to Deploy on AWS EC2

1. **Launch EC2 Instance**
   ```bash
   Instance Type: t2.medium
   AMI: Ubuntu 24.04 LTS
   ```

2. **Install Docker & Docker Compose**
   ```bash
   sudo apt update -y
   sudo apt install docker.io docker-compose -y
   sudo usermod -aG docker $USER
   newgrp docker
   ```

3. **Clone the Repository**
   ```bash
   git clone -b feature/docker-compose-aws https://github.com/Angad0691996/my_first_vehicle_dashboard.git
   cd my_first_vehicle_dashboard
   ```

4. **Run with Docker Compose**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

5. **Verify Containers**
   ```bash
   docker ps
   ```

6. **Access**
   - React Dashboard → `http://<EC2_PUBLIC_IP>:3000`
   - Flask Backend → `http://<EC2_PUBLIC_IP>:5000/latest`

---

## 📄 Documentation
 
📗 [EC2 Docker Compose Infrastructure (.pdf)](EC2_Docker_Compose_Infrastructure.pdf)

---

## 🌿 Git Branch

This EC2-based deployment is maintained in the branch:  
**`feature/docker-compose-aws`**

---

## 🧠 Summary

- End-to-end IoT data pipeline using Flask, React & MySQL  
- Data published via MQTT is displayed live on the dashboard  
- Fully containerized stack deployed on AWS EC2  
- Easy migration path to Kubernetes for production-grade scaling  

---

**Author:** Angad B.  
**Location:** Pune, India  
**Date:** October 2025  
