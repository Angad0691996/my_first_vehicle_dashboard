import os
import random
import json
import time
from datetime import datetime
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS IoT Core Details
ENDPOINT = "axpjfhduaw82h-ats.iot.ap-south-1.amazonaws.com"
CLIENT_ID = "angad_publisher"
TOPIC = "vehicle/data"
LWT_TOPIC = "vehicle/status"

# Absolute Paths to Certificates
ROOT_CA = os.path.abspath("creds/AmazonRootCA1.pem")
PRIVATE_KEY = os.path.abspath("creds/private.pem.key")
CERTIFICATE = os.path.abspath("creds/certificate.pem.crt")

# Initialize MQTT Client
mqtt_client = AWSIoTMQTTClient(CLIENT_ID)
mqtt_client.configureEndpoint(ENDPOINT, 8883)
mqtt_client.configureCredentials(ROOT_CA, PRIVATE_KEY, CERTIFICATE)

# Configure Last Will and Testament (LWT) to notify when subscriber is offline
mqtt_client.configureLastWill(LWT_TOPIC, "Subscriber is offline", QoS=1, retain=True)

# Connect to AWS IoT Core
mqtt_client.connect()
print("Connected to AWS IoT Core.")

# Function to Generate Custom Vehicle Payload
def generate_payload():
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S IST")
    location = f"{round(random.uniform(-90, 90), 6)}, {round(random.uniform(-180, 180), 6)}"
    return {
        "vehicle_ID": "Angad001",
        "Speed": random.randint(0, 120),
        "Battery_voltage": round(random.uniform(11.0, 14.0), 2),
        "Engine_Temp": random.randint(70, 120),
        "Fuel_Level": random.randint(0, 100),
        "timestamp": timestamp,
        "location": location
    }

# Publish Data Every 10 Seconds
while True:
    vehicle_data = generate_payload()
    payload = json.dumps(vehicle_data)

    # Try to publish data
    try:
        # Publish the data to the topic
        mqtt_client.publish(TOPIC, payload, QoS=1)
        print(f"Published: {payload}")
    except Exception as e:
        print(f"Failed to publish data: {e}")

    time.sleep(10)
