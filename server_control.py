# runs on PC/Laptop	Main function Start/Stop the Raspberry Pi server,	control server.py process	❌ No TCP/CP


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sys
import paramiko

# 🔹 SET THESE VALUES: Replace with your Raspberry Pi's details
RPI_HOST = "192.168.1.100"  # Raspberry Pi IP address
RPI_USER = "pi"  # Raspberry Pi username
RPI_PASSWORD = "raspberry"  # Raspberry Pi password (Change for security!)
SERVER_SCRIPT = "server.py"  # Name of the server script on Raspberry Pi


class ServerControlGUI(QMainWindow):
    def __init__(self):
        super(ServerControlGUI, self).__init__()
        self.exit_btn = None  # Button 4
        self.restart_btn = None  # Button 3
        self.stop_btn = None  # Button 2
        self.start_btn = None  # Button 1
        self.status_label = None  # Display
        self.setWindowTitle("Hexapod Server Control By sazid")
        self.setGeometry(200, 200, 400, 300)
        self.initUI()

    def initUI(self):
        # Server Status Label
        self.status_label = QLabel("🔴 Server is Stopped", self)
        self.status_label.setGeometry(120, 30, 200, 30)
        self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: red;")

        # Start Server Button
        self.start_btn = QPushButton("🟢 Start Server", self)
        self.start_btn.setGeometry(120, 80, 160, 40)
        self.start_btn.clicked.connect(self.start_server)

        # Stop Server Button
        self.stop_btn = QPushButton("🔴 Stop Server", self)
        self.stop_btn.setGeometry(120, 130, 160, 40)
        self.stop_btn.clicked.connect(self.stop_server)

        # Restart Server Button
        self.restart_btn = QPushButton("🔄 Restart Server", self)
        self.restart_btn.setGeometry(120, 180, 160, 40)
        self.restart_btn.clicked.connect(self.restart_server)

        # Exit Button
        self.exit_btn = QPushButton("🚪 Exit", self)
        self.exit_btn.setGeometry(120, 230, 160, 40)
        self.exit_btn.clicked.connect(self.close)

        self.setFixedSize(400, 300)  # Set window size
        self.show()

    def connect_ssh(self):
        """Establish an SSH connection to Raspberry Pi."""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(RPI_HOST, username=RPI_USER, password=RPI_PASSWORD)
            return ssh
        except Exception as e:
            self.status_label.setText("❌ SSH Connection Failed")
            self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: red;")
            print("SSH Error:", e)
            return None

    def start_server(self):
        """Start `server.py` on Raspberry Pi."""
        ssh = self.connect_ssh()
        if ssh:


            ssh.close()
            self.status_label.setText("🟢 Server is Running")
            self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: green;")

    def stop_server(self):
        """Stop `server.py` process on Raspberry Pi."""
        ssh = self.connect_ssh()
        if ssh:
            ssh.exec_command(f"pkill -f {SERVER_SCRIPT}")  # Kills the server process
            ssh.close()
            self.status_label.setText("🔴 Server is Stopped")
            self.status_label.setStyleSheet("font-size: 14px; font-weight: bold; color: red;")

    def restart_server(self):
        """Restart `server.py` on Raspberry Pi."""
        self.stop_server()
        self.start_server()


def run_gui():
    app = QApplication(sys.argv)
    win = ServerControlGUI()
    win.show()
    sys.exit(app.exec_())


run_gui()
