# Bluetooth Sensor to Gateway (Python)

## Description
This project implements a simple Bluetooth client-server application using Python and RFCOMM sockets. The client simulates a temperature sensor that sends data every 5 seconds, and the server receives and prints the data.

## Files
- server.py
- client.py

## Bluetooth MAC Address
40:23:43:82:EA:32

## Port Used
8

## How to Run
Run the server using: py server.py  
Run the client using: py client.py  

## Testing Result
The server started successfully and was able to listen for incoming Bluetooth connections. However, the client could not connect when running on the same laptop. This is because Bluetooth RFCOMM communication on Windows does not support using the same device as both client and server in this setup. A full test requires two paired Bluetooth devices.

## Screenshot
Screenshots are included showing the server running successfully and the client connection failure.

## Reflection
I learned how to create Bluetooth socket communication in Python and how client-server communication works in IoT systems. The most difficult part was testing Bluetooth communication on a single device because it requires two separate devices. Bluetooth can be used in IoT for short-range communication between sensors, smart devices, and local gateways. In practice, Bluetooth is used for short-range, low-power communication between nearby devices, while WiFi is used for longer range, higher speed, and internet-based communication.