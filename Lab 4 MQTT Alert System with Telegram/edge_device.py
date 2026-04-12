import socket
import paho.mqtt.client as mqtt

host = "127.0.0.1"
port = 5000

broker = "broker.emqx.io"
topic = "savonia/iot/temperature"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

mqtt_client = mqtt.Client()
mqtt_client.connect(broker, 1883)

print("Waiting for sensor connection...")

client_socket, addr = server.accept()
print("Sensor connected from:", addr)

try:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        temperature = data.decode("utf-8")
        print("Received from sensor:", temperature)

        mqtt_client.publish(topic, temperature)
        print("Published to MQTT:", temperature)

except OSError as e:
    print("Connection error:", e)

client_socket.close()
server.close()