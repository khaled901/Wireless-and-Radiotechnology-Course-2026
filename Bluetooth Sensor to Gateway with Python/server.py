import socket

server_mac = "40:23:43:82:EA:32"
port = 8

server = socket.socket(
    socket.AF_BLUETOOTH,
    socket.SOCK_STREAM,
    socket.BTPROTO_RFCOMM
)

server.bind((server_mac, port))
server.listen(1)

print("Waiting for Bluetooth client connection...")

client, addr = server.accept()
print(f"Connected to: {addr}")

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("Received:", data.decode("utf-8"))

except OSError:
    print("Connection closed.")

client.close()
server.close()