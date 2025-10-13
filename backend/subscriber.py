import threading
from flask import Flask, jsonify
from flask_cors import CORS
import paho.mqtt.client as paho
import ssl
import json
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
from flask import jsonify



# Global variable to store the latest payload for the API
latest_payload = {}

# MySQL config (update with your username, password, host)
db_config = {
    'user': 'vehicledbuser',
    'password': 'Mycloud@25',
    'host': 'localhost',
    'database': 'vehicle_dashboard',
    'raise_on_warnings': True
}

# Initialize MySQL connection
def get_db_connection():
    try:
        cnx = mysql.connector.connect(**db_config)
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist, please create it")
        else:
            print(err)
        return None

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    client.subscribe("vehicle/data", qos=1)
from datetime import datetime

def on_message(client, userdata, msg):
    global latest_payload
    print("Message received:")
    print("  Topic:", msg.topic)
    try:
        payload = json.loads(msg.payload.decode())
        latest_payload = payload
        print("  Payload:", json.dumps(payload, indent=2))

        # Convert timestamp from "13/10/2025 13:31:06 IST" to MySQL format
        raw_timestamp = payload.get("timestamp", "").replace(" IST", "")
        dt_obj = datetime.strptime(raw_timestamp, "%d/%m/%Y %H:%M:%S")
        mysql_timestamp = dt_obj.strftime("%Y-%m-%d %H:%M:%S")

        # Insert into MySQL database
        cnx = get_db_connection()
        if cnx:
            cursor = cnx.cursor()
            insert_stmt = (
                "INSERT INTO vehicle_logs "
                "(vehicle_ID, Speed, Battery_voltage, Engine_Temp, Fuel_Level, timestamp, location) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )
            data = (
                payload.get("vehicle_ID"),
                float(payload.get("Speed", 0)),
                float(payload.get("Battery_voltage", 0)),
                float(payload.get("Engine_Temp", 0)),
                float(payload.get("Fuel_Level", 0)),
                mysql_timestamp,           # Use converted timestamp here
                payload.get("location")
            )
            cursor.execute(insert_stmt, data)
            cnx.commit()
            cursor.close()
            cnx.close()
            print("  Data inserted into database.")

    except json.JSONDecodeError:
        print("  Invalid JSON payload")
    except Exception as e:
        print("  Error inserting into database:", e)


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
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

@app.route('/api/logs', methods=['GET'])
def get_logs():
    cnx = get_db_connection()
    cursor = cnx.cursor(dictionary=True)
    cursor.execute("SELECT * FROM vehicle_logs ORDER BY timestamp DESC LIMIT 50")
    rows = cursor.fetchall()
    cursor.close()
    cnx.close()
    return jsonify(rows)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    mqttc.connect(awshost, awsport, keepalive=60)
    mqttc.loop_forever()
