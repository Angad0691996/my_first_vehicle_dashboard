import threading
from flask import Flask, jsonify
from flask_cors import CORS
import paho.mqtt.client as paho
import ssl
import json

# Global variable to hold the latest vehicle data
latest_payload = {}

# --- MQTT Setup and Handlers ---

def on_connect(client, userdata, flags, rc):
    print("MQTT Connected with result code: " + str(rc))
    # Subscribe inside on_connect to auto-re-subscribe on reconnect
    client.subscribe("vehicle/data", qos=1)

def on_message(client, userdata, msg):
    global latest_payload
    # print("Message received on topic:", msg.topic) # Can be noisy in production logs
    try:
        # Decode and parse the JSON payload
        payload = json.loads(msg.payload.decode())
        latest_payload = payload
        # print("Payload updated:", json.dumps(payload, indent=2))
    except json.JSONDecodeError:
        print("Error: Invalid JSON payload received")

# --- Configuration and Initialization ---

awshost = "axpjfhduaw82h-ats.iot.ap-south-1.amazonaws.com"
awsport = 8883
# These paths are relative to the working directory, which Gunicorn will set
caPath = "creds/AmazonRootCA1.pem"
certPath = "creds/certificate.pem.crt"
keyPath = "creds/private.pem.key"

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

# Set up TLS/SSL for AWS IoT connection
mqttc.tls_set(ca_certs=caPath,
              certfile=certPath,
              keyfile=keyPath,
              tls_version=ssl.PROTOCOL_TLSv1_2)

# Connect and start the MQTT loop in a background thread
def start_mqtt_client():
    try:
        mqttc.connect(awshost, awsport, keepalive=60)
        # Use loop_start() to run the loop in its own background thread
        mqttc.loop_start() 
        print("MQTT client loop started in a background thread.")
    except Exception as e:
        print(f"Error connecting to MQTT: {e}")


# --- Flask Application Setup ---

app = Flask(__name__)
CORS(app) # Enable CORS for your React frontend

@app.route('/latest')
def get_latest():
    """API endpoint for the React frontend to fetch the latest data."""
    return jsonify(latest_payload)

# -----------------------------------------------------------------
# 🎯 CRITICAL PRODUCTION BLOCK 
# -----------------------------------------------------------------

# This code runs when the script is imported by Gunicorn
# The start_mqtt_client() function will execute once,
# starting the MQTT loop in a separate thread.
print("Starting up application...")
start_mqtt_client()
print("Application ready to serve requests via Gunicorn.")

# Gunicorn will now manage and serve the 'app' Flask instance.

# -----------------------------------------------------------------
# Removed the `if __name__ == "__main__":` block with app.run() and threading.
# -----------------------------------------------------------------