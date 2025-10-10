import React, { useEffect, useState } from 'react';
import './App.css';
import car from './car.png'; // import car image
import LocationMap from './LocationMap';


function App() {
  const [vehicleData, setVehicleData] = useState(null);

  useEffect(() => {
    const fetchData = () => {
      fetch('/latest')
        .then(res => res.json())
        .then(data => setVehicleData(data))
        .catch(err => console.error('Error fetching vehicle data:', err));
    };

    fetchData();
    const intervalId = setInterval(fetchData, 2000);
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1 className="heading">SAMSAN Technishque Vehicle Dashboard</h1>
      </header>
      <div className="dashboard-row">
        {vehicleData && Object.keys(vehicleData).length > 0 ? (
          <>
            <div className="dashboard">
              <div className="dashboard-card">
                <span className="label">Vehicle ID:</span>
                <span className="value">{vehicleData.vehicle_ID}</span>
              </div>
              <div className="dashboard-card">
                <span className="label">Speed:</span>
                <span className="value">{vehicleData.Speed} km/h</span>
              </div>
              <div className="dashboard-card">
                <span className="label">Timestamp:</span>
                <span className="value">{vehicleData.timestamp}</span>
              </div>
              <div className="dashboard-card">
                <span className="label">Location:</span>
                <LocationMap
                  lat={parseFloat(vehicleData.location.split(',')[0].trim())}
                  lng={parseFloat(vehicleData.location.split(',')[1].trim())}
                />
              </div>
            </div>
            <div className="car-image-container">
              <img className="car-image" src={car} alt="Car" />
            </div>
          </>
        ) : (
          <p>Loading vehicle data...</p>
        )}
      </div>
    </div>
  );
}

export default App;
