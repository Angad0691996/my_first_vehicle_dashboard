| Task                              | Command                                               | Description                               |
| --------------------------------- | ----------------------------------------------------- | ----------------------------------------- |
| 🧩 **Run in Dev Mode (Windows)**  | `docker compose -f docker-compose.dev.yml up --build` | Builds backend & frontend from local code |
| 🚀 **Run in Prod Mode (Ubuntu)**  | `docker compose -f docker-compose.prod.yml up -d`     | Pulls prebuilt images from Docker Hub     |
| 🧹 **Tear Down & Remove Volumes** | `docker compose down -v`                              | Stops and removes containers + volumes    |
