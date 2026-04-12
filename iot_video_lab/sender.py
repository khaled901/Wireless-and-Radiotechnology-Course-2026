import socket
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "127.0.0.1"   # للتجربة على نفس اللاب
PORT = 5001
VIDEO_FOLDER = os.path.join(BASE_DIR, "videos")
CHECK_INTERVAL = 5

os.makedirs(VIDEO_FOLDER, exist_ok=True)
print("Watching folder:", VIDEO_FOLDER)
print("Sender started. Watching video folder...")

def is_file_ready(filepath, wait_seconds=2):
    try:
        size1 = os.path.getsize(filepath)
        time.sleep(wait_seconds)
        size2 = os.path.getsize(filepath)
        return size1 == size2 and size1 > 0
    except Exception:
        return False

def send_file(filepath):
    filename = os.path.basename(filepath)

    if not os.path.exists(filepath):
        return False

    if not is_file_ready(filepath):
        print(f"File still being written, skipping for now: {filename}")
        return False

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))

        client.sendall(filename.encode())
        response = client.recv(1024)

        if response != b"FILENAME_OK":
            print(f"Receiver did not accept filename for {filename}")
            client.close()
            return False

        with open(filepath, "rb") as f:
            while True:
                data = f.read(4096)
                if not data:
                    break
                client.sendall(data)

        client.sendall(b"EOF")

        response = client.recv(1024)
        client.close()

        if response == b"OK":
            print(f"Transfer confirmed: {filename}")
            os.remove(filepath)
            print(f"Deleted local file: {filename}\n")
            return True
        else:
            print(f"No valid confirmation for {filename}")
            return False

    except Exception as e:
        print(f"Error sending {filename}: {e}")
        return False

while True:
    files = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(".mp4")]
    files.sort()

    for file in files:
        filepath = os.path.join(VIDEO_FOLDER, file)
        send_file(filepath)

    time.sleep(CHECK_INTERVAL)