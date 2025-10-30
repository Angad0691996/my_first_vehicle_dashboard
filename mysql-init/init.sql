CREATE TABLE IF NOT EXISTS vehicle_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_ID VARCHAR(50),
    Speed FLOAT,
    Battery_voltage FLOAT,
    Engine_Temp FLOAT,
    Fuel_Level FLOAT,
    timestamp DATETIME,
    location VARCHAR(100)
);
