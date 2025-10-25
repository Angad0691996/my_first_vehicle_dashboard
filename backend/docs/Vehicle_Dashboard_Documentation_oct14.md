# Vehicle Dashboard Project Documentation

## 1. Database Integration for Vehicle History
- Integrated MySQL database to store vehicle telemetry data persistently.
- Created a `vehicle_logs` table to save fields like vehicle ID, speed, battery voltage, engine temperature, fuel level, timestamp, and location.
- Modified backend MQTT subscriber in Flask to parse incoming telemetry JSON messages, convert timestamps, and insert records into the database.
- Exposed a new REST API endpoint `/api/logs` in Flask to retrieve the latest 50 historical vehicle log entries as a JSON array.

## 2. React Frontend: History Display
- Added a new React component `VehicleLogs` to fetch and render historical vehicle telemetry data from the `/api/logs` endpoint.
- Implemented data fetching using React's `useEffect` hook and controlled loading states.
- Rendered vehicle history in a table with all telemetry fields and timestamps.
- Enabled tab-based navigation to toggle between:
  - **Dashboard**: Current real-time vehicle data display.
  - **History**: Past telemetry data from the database shown in `VehicleLogs`.

## 3. UI and UX Enhancements
- Created tab buttons (“Dashboard”, “History”) in `App.js` with state management (`useState`) to switch views.
- Added CSS styling controls for tab button size, hover effects, and disabled state for better user experience.
- Preserved existing features such as the map modal displaying real-time vehicle location.

## 4. Version Control Workflow Updates
- Documented common Git workflow for managing changes:
  - Staging modified and new files with `git add`.
  - Committing changes with meaningful messages.
  - Pushing commits to feature branches.
- Explained the meaning of “Changes not staged for commit” and “Untracked files” messages to avoid confusion.

---

## Next Steps (Planned)
- Add better styling and responsiveness to the vehicle logs table.
- Implement filtering, sorting, and pagination of historical data.
- Possibly add authentication to protect backend APIs.
- Improve error handling and reconnection logic for backend and frontend.
- Explore data visualization for historical telemetry trends and patterns.
