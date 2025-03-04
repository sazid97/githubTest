# RUNS On RRaspberry Pi	Process commands & move servos control Hexapod servos	✅ use TCP/CP
import socket
import json
import time
from adafruit_servokit import ServoKit

# Initialize PCA9685 (16-channel PWM driver)
kit = ServoKit(channels=16)

# Hexapod leg servos mapping (Modify based servo connections)
SERVO_MAP = {
    "forward": [0, 3, 6, 9, 12, 15],  # servo channels for movement
    "backward": [1, 4, 7, 10, 13, 16],
    "left": [2, 5, 8, 11, 14, 17],
    "right": [0, 3, 6, 9, 12, 15],  # as needed
    "stand_up": [0, 1, 2, 3, 4, 5],  # stand-up servos
    "sit_down": [6, 7, 8, 9, 10, 11]
}


# Function to move servos
def move_servos(action):
    if action in SERVO_MAP:
        for servo in SERVO_MAP[action]:
            kit.servo[servo].angle = 90  # Move to 90 degrees as an example
            time.sleep(0.1)  # Delay for smooth movement
        print(f"{action} command executed")
    else:
        print("Invalid Command")


# Start TCP Server
def start_server():
    HOST = "0.0.0.0"  # Listen on all network interfaces
    PORT = 5002  # Communication port
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"🚀 Hexapod Server Running on {HOST}:{PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"✅ Connection from {addr}")

        data = client_socket.recv(1024).decode()
        if not data:
            break

        command = json.loads(data).get("command")
        print(f"📩 Received Command: {command}")

        move_servos(command)  # Execute servo movement

        client_socket.sendall(json.dumps({"status": "success"}).encode())  # Send response
        client_socket.close()


if __name__ == "__main__":
    start_server()




