import socket
import random
import time

# استبدل هذا بعنوان Bluetooth MAC الخاص بالسيرفر
SERVER_MAC_ADDRESS = "40-23-43-82-EA-32"
PORT = 4

def main():
    client = socket.socket(
        socket.AF_BLUETOOTH,
        socket.SOCK_STREAM,
        socket.BTPROTO_RFCOMM
    )

    try:
        client.connect((SERVER_MAC_ADDRESS, PORT))
        print("Connected to Bluetooth server")

        while True:
            temperature = round(random.uniform(20.0, 30.0), 1)
            message = f"Temperature: {temperature} C"
            client.send(message.encode("utf-8"))
            print("Sent:", message)
            time.sleep(5)

    except OSError as e:
        print("Bluetooth client error:", e)

    finally:
        client.close()
        print("Client closed.")

if __name__ == "__main__":
    main()