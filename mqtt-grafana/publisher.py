import time
import random
import json
import paho.mqtt.client as mqtt

BROKER = "broker.emqx.io"
PORT = 1883
TOPIC = "savonia/khaled/temperature2"  # غيرنا التوبيك عشان نبدأ من جديد
CLIENT_ID = f"khaled_publisher_{random.randint(1000,9999)}"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected successfully to broker")
    else:
        print(f"Connection failed with code {rc}")

def on_publish(client, userdata, mid, properties=None):
    print(f"Message published, mid={mid}")

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(BROKER, PORT, 60)
client.loop_start()

print(f"Connected to MQTT broker: {BROKER}:{PORT}")
print(f"Publishing to topic: {TOPIC}")

try:
    while True:
        temperature = round(random.uniform(20, 35), 2)

        payload = {
            "temperature": temperature
        }

        result = client.publish(TOPIC, json.dumps(payload))
        result.wait_for_publish()

        print(f"Published: {payload}")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nPublisher stopped.")

finally:
    client.loop_stop()
    client.disconnect()