import React, { useEffect, useState } from 'react';

function VehicleLogs() {
  const [logs, setLogs] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`${process.env.REACT_APP_BACKEND_URL}/api/logs`)
      .then(res => res.json())
      .then(data => {
        setLogs(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Error fetching logs:", err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading logs...</p>;
  }

  if (!logs.length) {
    return <p>No historical logs found.</p>;
  }

  return (
    <table>
      <thead>
        <tr>
          <th>Vehicle ID</th>
          <th>Speed</th>
          <th>Battery Voltage</th>
          <th>Engine Temp</th>
          <th>Fuel Level</th>
          <th>Timestamp</th>
          <th>Location</th>
        </tr>
      </thead>
      <tbody>
        {logs.map((log, idx) => (
          <tr key={idx}>
            <td>{log.vehicle_ID}</td>
            <td>{log.Speed}</td>
            <td>{log.Battery_voltage}</td>
            <td>{log.Engine_Temp}</td>
            <td>{log.Fuel_Level}</td>
            <td>{log.timestamp}</td>
            <td>{log.location}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default VehicleLogs;
