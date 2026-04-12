import socket
import time
import random

HOST = '172.20.10.2' 
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected to server")

while True:
    temperature = round(random.uniform(20.0, 30.0), 2)
    message = f"Temperature: {temperature} C"

    client.send(message.encode())
    print("Sent:", message)

    time.sleep(5)