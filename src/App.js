import React, { useEffect, useState } from 'react';
import './App.css';
import car from './car.png';
import LocationMap from './LocationMap';

function App() {
  const [vehicleData, setVehicleData] = useState(null);
  const [showMap, setShowMap] = useState(false);

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

  if (!vehicleData || Object.keys(vehicleData).length === 0) {
    return (
      <div className="loading-container">
        <p className="loading-text">Loading vehicle data...</p>
      </div>
    );
  }

  const [lat, lng] = vehicleData.location
    ? vehicleData.location.split(',').map(coord => parseFloat(coord.trim()))
    : [0, 0];

  return (
    <div className="App">
      <header className="app-header">
        <h1 className="heading">SAMSAN Technishque Vehicle Dashboard</h1>
      </header>

      <main className="dashboard-row">
        {/* LEFT SIDE - DATA */}
        <section className="dashboard">
          {[
            { label: 'Vehicle ID', value: vehicleData.vehicle_ID },
            { label: 'Speed', value: `${vehicleData.Speed} km/h` },
            { label: 'Battery Voltage', value: `${vehicleData.Battery_voltage} V` },
            { label: 'Engine Temp', value: `${vehicleData.Engine_Temp} °C` },
            { label: 'Fuel Level', value: `${vehicleData.Fuel_Level} %` },
            { label: 'Timestamp', value: vehicleData.timestamp }
          ].map((item, idx) => (
            <div className="dashboard-card" key={idx}>
              <span className="label">{item.label}:</span>
              <span className="value">{item.value}</span>
            </div>
          ))}

          <div className="dashboard-card">
            <span className="label">Location:</span>
            <button className="location-btn" onClick={() => setShowMap(true)}>
              🌍 View Location
            </button>
          </div>
        </section>

        {/* RIGHT SIDE - CAR IMAGE */}
        <aside className="visuals">
          <div className="car-image-container">
            <img className="car-image" src={car} alt="Car" />
          </div>
        </aside>
      </main>

      {/* FULL-SCREEN MAP MODAL */}
      {showMap && (
        <div className="map-modal" onClick={() => setShowMap(false)}>
          <div className="map-content" onClick={(e) => e.stopPropagation()}>
            <button className="close-btn" onClick={() => setShowMap(false)}>
              ✖
            </button>
            <LocationMap lat={lat} lng={lng} />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
