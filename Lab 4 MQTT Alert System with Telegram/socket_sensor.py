import socket
import random
import time

host = "127.0.0.1"
port = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print("Connected to edge device")

try:
    while True:
        temperature = round(random.uniform(20.0, 30.0), 1)
        message = str(temperature)
        client.send(message.encode("utf-8"))
        print("Sent temperature:", message)
        time.sleep(5)

except OSError as e:
    print("Connection error:", e)

client.close()