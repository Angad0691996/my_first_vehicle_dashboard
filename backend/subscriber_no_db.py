import threading
from flask import Flask, jsonify
from flask_cors import CORS
import paho.mqtt.client as paho
import ssl
import json

latest_payload = {}

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("vehicle/data", qos=1)

def on_message(client, userdata, msg):
    global latest_payload
    print("Message received:")
    print("  Topic:", msg.topic)
    try:
        payload = json.loads(msg.payload.decode())
        latest_payload = payload
        print("  Payload:", json.dumps(payload, indent=2))
    except json.JSONDecodeError:
        print("  Invalid JSON payload")

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "axpjfhduaw82h-ats.iot.ap-south-1.amazonaws.com"
awsport = 8883
caPath = "creds/AmazonRootCA1.pem"
certPath = "creds/certificate.pem.crt"
keyPath = "creds/private.pem.key"

mqttc.tls_set(ca_certs=caPath,
              certfile=certPath,
              keyfile=keyPath,
              tls_version=ssl.PROTOCOL_TLSv1_2)

# Flask app to serve latest payload
app = Flask(__name__)
CORS(app)

@app.route('/latest')
def get_latest():
    return jsonify(latest_payload)

def run_flask():
    app.run(port=5000, debug=False, use_reloader=False)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    mqttc.connect(awshost, awsport, keepalive=60)
    mqttc.loop_forever()