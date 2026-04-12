import socket
import random
import time

server_mac = "40:23:43:82:EA:32"
port = 8

client = socket.socket(
    socket.AF_BLUETOOTH,
    socket.SOCK_STREAM,
    socket.BTPROTO_RFCOMM
)

client.connect((server_mac, port))

print("Connected to Bluetooth server")

try:
    while True:
        temperature = round(random.uniform(20.0, 30.0), 1)
        message = f"Temperature: {temperature} C"
        client.send(message.encode("utf-8"))
        print("Sent:", message)
        time.sleep(5)

except OSError:
    print("Connection closed.")

client.close()