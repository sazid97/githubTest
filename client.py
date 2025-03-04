# # can runs on PC/Laptop	Send commands to Raspberry Pi, control Hexapod movements	✅ Use TCP/CP
#
#
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
# import sys
# import socket
# import json
#
# RPI_IP = "192.168.1.100"  # Raspberry Pi's IP address needed
# PORT = 5002   # port number needed
#
#
# class HexapodGUI(QMainWindow):
#     def __init__(self):
#         super(HexapodGUI, self).__init__()
#         self.label = None
#         self.setWindowTitle("HEXAPOD Control Panel")
#         self.setGeometry(200, 200, 500, 500)
#         self.initGUI()
#
#     def initGUI(self):
#         self.label = QLabel("🔴 Not Connected", self)
#         self.label.move(200, 20)
#         self.label.setStyleSheet("font-size: 14px; font-weight: bold; color: red;")
#
#         # Button Layout
#         self.Forward = QPushButton("▶️ Forward", self)
#         self.Forward.setGeometry(190, 60, 120, 40)
#         self.Forward.clicked.connect(lambda: self.send_command("forward"))
#
#         self.Backward = QPushButton("🔙 Backward", self)
#         self.Backward.setGeometry(190, 120, 120, 40)
#         self.Backward.clicked.connect(lambda: self.send_command("backward"))
#
#         self.Left = QPushButton("◀️ Left", self)
#         self.Left.setGeometry(60, 90, 120, 40)
#         self.Left.clicked.connect(lambda: self.send_command("left"))
#
#         self.Right = QPushButton("▶️ Right", self)
#         self.Right.setGeometry(320, 90, 120, 40)
#         self.Right.clicked.connect(lambda: self.send_command("right"))
#
#         self.StandUp = QPushButton("⏫ Stand Up", self)
#         self.StandUp.setGeometry(60, 180, 120, 40)
#         self.StandUp.clicked.connect(lambda: self.send_command("stand_up"))
#
#         self.SitDown = QPushButton("⏬ Sit Down", self)
#         self.SitDown.setGeometry(320, 180, 120, 40)
#         self.SitDown.clicked.connect(lambda: self.send_command("sit_down"))
#
#         self.exit = QPushButton("🚪 Exit", self)
#         self.exit.setGeometry(190, 240, 120, 40)
#         self.exit.clicked.connect(self.close)
#
#     def send_command(self, command):
#         try:
#             client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             client_socket.connect((RPI_IP, PORT))
#             message = json.dumps({"command": command})
#             client_socket.sendall(message.encode())
#
#             response = client_socket.recv(1024).decode()
#             client_socket.close()
#
#             self.label.setText(f"✅ Command Sent: {command}")
#             self.label.setStyleSheet("font-size: 14px; font-weight: bold; color: green;")
#         except Exception as e:
#             self.label.setText("❌ Connection Failed")
#             self.label.setStyleSheet("font-size: 14px; font-weight: bold; color: red;")
#             print("Error:", e)
#
#
# def run_gui():
#     app = QApplication(sys.argv)
#     win = HexapodGUI()
#     win.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == "__main__":
#     run_gui()

#
