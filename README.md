# 🚗 Vehicle Dashboard – Containerized DevOps Architecture

A full-stack **Vehicle Telemetry Dashboard** demonstrating a **containerized DevOps architecture** using **Docker Compose**.
It includes three core services running in isolated containers for modular, portable, and cloud-ready deployment.

---

## 🧩 Core Components

| Service | Description | Tech Stack | Default Port |
|----------|-------------|-------------|---------------|
| 🖥️ **React Dashboard (Frontend)** | Displays live and historical vehicle data | React + Nginx | 3000 → 80 |
| ⚙️ **Flask Backend API (Subscriber)** | Subscribes to AWS IoT MQTT data & serves REST APIs | Python (Flask, Paho-MQTT) | 5000 |
| 🗄️ **MySQL Database** | Stores telemetry history and metadata | MySQL 8.0 | 3307 → 3306 |

---

## 🏗️ Architecture Overview

```
User Browser (http://localhost:3000)
        |
        | HTTP Requests
        v
React Dashboard (Nginx)
        |
        | Fetch API calls → http://localhost:5000
        v
Flask Backend API (Subscriber)
        |
        | Docker Network Connection
        v
MySQL Database (vehicle_dashboard)
```

All services run within a shared Docker network (default: `vehicle_dashboard_default`), ensuring seamless communication between containers.

---

## 🧱 Running Containers

| Container | Image | Ports | Status |
|------------|--------|--------|--------|
| `react-dashboard` | `angad696/react-dashboard:latest` | `3000:80` | 🟢 Running |
| `backend-subscriber` | `angad696/backend-subscriber:latest` | `5000:5000` | 🟢 Running |
| `mysql-db` | `mysql:8.0` | `3307:3306` | 🟢 Running |

---

## 🧰 Development vs Production

| Environment | Compose File | Build Source | Description |
|--------------|---------------|---------------|--------------|
| 🧪 **Windows / Development** | `docker-compose.dev.yml` | Local Dockerfile builds | Used to build new images and test updates |
| 🚀 **Ubuntu / Production** | `docker-compose.prod.yml` | Uses pre-built Docker Hub images | Pulls ready-to-run containers for deployment |

---

## ⚙️ Prerequisites

- **Docker** (v27+)
- **Docker Compose Plugin** (v2.40+)
- **Git**

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Angad0691996/my_first_vehicle_dashboard.git
cd my_first_vehicle_dashboard
```

### 2️⃣ Start Containers
- **For local development (build images):**
  ```bash
  docker compose -f docker-compose.dev.yml up -d --build
  ```
- **For Ubuntu / production (use pre-built images):**
  ```bash
  docker compose -f docker-compose.prod.yml up -d
  ```

### 3️⃣ Verify Containers
```bash
docker ps
```

You should see all three services running.

---

## 🗃️ Database Setup

The MySQL database initializes automatically if a `mysql-init` folder with SQL scripts exists.

If not, create the `vehicle_logs` table manually:
```sql
CREATE TABLE vehicle_logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  vehicle_ID VARCHAR(50),
  Speed FLOAT,
  Battery_voltage FLOAT,
  Engine_Temp FLOAT,
  Fuel_Level FLOAT,
  timestamp DATETIME,
  location VARCHAR(100)
);
```

Access the MySQL shell:
```bash
docker exec -it mysql-db mysql -u vehicledbuser -p
```

---

## 🔧 Environment Variables (.env)

```
MYSQL_ROOT_PASSWORD=Mycloud@25
MYSQL_DATABASE=vehicle_dashboard
MYSQL_USER=vehicledbuser
MYSQL_PASSWORD=Mycloud@25

DB_HOST=mysql-db
DB_USER=vehicledbuser
DB_PASSWORD=Mycloud@25
DB_NAME=vehicle_dashboard

REACT_APP_BACKEND_URL=http://localhost:5000
```

---

## 🌿 Git Workflow

```bash
git checkout -b feature/devops-architecture-setup
git add .
git commit -m "Containerized full-stack setup"
git push -u origin feature/devops-architecture-setup
```

Then open a **Pull Request** on GitHub.

---

## 🖼️ Screenshots

| Dashboard | History Tab | Map View | Architecture |
|------------|-------------|-----------|---------------|
| ![](assets/dashboard-preview.png) | ![](assets/dashboard-tab2-history.png) | ![](assets/location.png) | ![](assets/Web%20App%20Architecture%20Flowchart.png) |

---

## 🧠 Highlights

- ✅ Fully **containerized** full-stack app  
- 🔁 **Seamless data flow** between React → Flask → MySQL  
- 💾 **Persistent volumes** for MySQL storage  
- 🌐 Works on **Windows & Ubuntu**  
- ☁️ Ready for **CI/CD and cloud deployment**

---

## 🤝 Contribute

Contributions and feature requests are welcome!  
Fork the repo, open issues, or submit pull requests.

---

## 📄 License

[MIT License](LICENSE)

---

> **Author:** Angad B.  
> **Location:** Pune, India  
> 💡 *“Building the bridge between IoT, Cloud & DevOps.”*
