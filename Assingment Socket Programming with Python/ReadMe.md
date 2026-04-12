# TCP Client–Server Communication Project

## Description

This project demonstrates a simple TCP socket communication system using Python.
It was developed as a practical lab to understand how client–server communication works.

The server receives data from a client that simulates sensor readings such as temperature.

This lab was completed collaboratively by:

* Khaled Ahmed
* Ammar Khalil

---

## How to Run

### 1. Run the Server

On the server machine:

```bash
python server.py
```

---

### 2. Run the Client

On the client machine:

1. Update the server IP address in `client.py`
2. Run:

```bash
python client.py
```

---

## Features

* TCP socket communication
* Real-time data transfer between two devices
* Random temperature generation
* Data sent every 5 seconds

---

## Testing

### Test 1: Same WiFi Network

* Server and client connected on the same WiFi
* Communication successful

### Test 2: Mobile Hotspot

* Tested using a mobile hotspot
* Communication successful between two devices

---

## Screenshot

![Client-Server Communication](client_terminal.jpeg)
![Client-Server Communication](server_terminal.jpeg)

---

## Notes

* Make sure both devices are connected to the same network
* Ensure the correct IP address is used
* The server must be running before starting the client

---

## Authors

* Khaled Ahmed
* Ammar Khalil
