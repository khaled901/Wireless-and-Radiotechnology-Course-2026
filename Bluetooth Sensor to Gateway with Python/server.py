import socket

PORT = 4

def main():
    server = socket.socket(
        socket.AF_BLUETOOTH,
        socket.SOCK_STREAM,
        socket.BTPROTO_RFCOMM
    )

    try:
        server.bind(("", PORT))
        server.listen(1)

        print("Waiting for Bluetooth client connection...")

        client, addr = server.accept()
        print(f"Connected to: {addr}")

        while True:
            data = client.recv(1024)
            if not data:
                break

            print("Received:", data.decode("utf-8"))

        client.close()

    except OSError as e:
        print("Bluetooth server error:", e)

    finally:
        server.close()
        print("Server closed.")

if __name__ == "__main__":
    main()