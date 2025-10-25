

# 🚗 Vehicle Dashboard - Containerized DevOps Architecture

A full-stack **Vehicle Telemetry Dashboard** showcasing a containerized DevOps architecture with Docker Compose.  
It includes three core services running in isolated containers:

- 🖥️ **React Dashboard (Frontend)** served via Nginx  
- ⚙️ **Flask Backend API (Subscriber)** handling telemetry data  
- 🗄️ **MySQL Database** for persistent storage  

---

## 🧩 Architecture Overview

The setup runs within Docker Compose’s default network:  
**`project1_containerize_default`**

```
User Browser (http://localhost:3000)
        |
        | HTTP Requests
        v
React Dashboard (Nginx) — Container (Port: 3000 → 80)
        |
        | Fetch API calls → http://localhost:5000
        v
Flask Backend API — Container (Port: 5000 → 5000)
        |
        | Connects via Docker Network
        v
MySQL Database — Container (Port: 3307 → 3306)
```

---

## 🧱 Running Containers

| Container Name                     | Image                                      | Ports Mapping         | Status       |
|------------------------------------|--------------------------------------------|------------------------|--------------|
| `react-dashboard`                  | project1_containerize-react-dashboard       | 0.0.0.0:3000 → 80/tcp  | 🟢 Running |
| `backend-subscriber`               | project1_containerize-backend-subscriber    | 0.0.0.0:5000 → 5000/tcp | 🟢 Running |
| `project1_containerize-mysql-db-1` | mysql:8.0                                  | 0.0.0.0:3307 → 3306/tcp | 🟢 Running |

---

## 📁 Assets in `/assets` Directory

| File Name                      | Description |
|--------------------------------|-------------|
| `dashboard-preview.png`        | Preview of the main vehicle dashboard UI |
| `dashboard-tab2-history.png`   | History tab snapshot |
| `location.png`                 | Map view showing vehicle location |
| `Web App Architecture Flowchart.png` | Detailed system architecture flowchart |

---

## ⚙️ Prerequisites

- Docker & Docker Compose (Docker Desktop recommended)
- Git (for version control)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Angad0691996/my_first_vehicle_dashboard.git
cd my_first_vehicle_dashboard
```

### 2️⃣ Build and Start the Containers

```bash
docker-compose up -d
```

### 3️⃣ Check Running Containers

```bash
docker ps
```

✅ You should see output similar to the container table above.

---

## 🗃️ Database Setup

When running for the first time, create the MySQL table `vehicle_logs`:

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

Connect using:
```bash
docker exec -it project1_containerize-mysql-db-1 mysql -u vehicledbuser -p
```
Then run the SQL commands above.

---

## 🧰 Development Workflow

- Update **React frontend** in the `react-dashboard` directory → rebuild the image.
- Update **Flask backend** in the `backend-subscriber` directory → rebuild the image.
- Database credentials and backend URLs are defined in `.env`.

Rebuild containers after making changes:
```bash
docker-compose build
docker-compose up -d
```

---

## 🌿 Git Workflow

For feature development:

```bash
git checkout -b feature/devops-architecture-setup
```

Commit and push changes:
```bash
git add .
git commit -m "Add Dockerized full-stack setup"
git push -u origin feature/devops-architecture-setup
```

Then create a **Pull Request** on GitHub.

---

## 🖼️ Screenshots

| Dashboard | History Tab | Map View | Architecture |
|------------|-------------|-----------|---------------|
| ![](assets/dashboard-preview.png) | ![](assets/dashboard-tab2-history.png) | ![](assets/location.png) | ![](assets/Web%20App%20Architecture%20Flowchart.png) |

---

## 🧠 Summary

This project demonstrates:
- Containerized full-stack setup using **Docker Compose**
- Seamless data flow between **React → Flask → MySQL**
- Persistent storage via **Docker volumes**
- A foundation for **DevOps CI/CD** pipelines and cloud deployment

---

## 🤝 Contribute

Contributions, feature requests, and bug reports are welcome.  
Feel free to fork this repo and submit a pull request.

---

## 📄 License

[MIT License](LICENSE)

---

> **Author:** Angad B.  
> **Location:** Pune, India  
> *"Building the bridge between IoT, Cloud & DevOps."*
