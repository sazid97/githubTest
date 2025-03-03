GUI main.py

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
import sys


class HexapodGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Hexapod Robot Controller")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Hexapod Control Panel", self)
        layout.addWidget(self.label)

        self.move_forward_btn = QPushButton("Move Forward", self)
        self.move_forward_btn.clicked.connect(self.move_forward)
        layout.addWidget(self.move_forward_btn)

        self.stop_btn = QPushButton("Stop", self)
        self.stop_btn.clicked.connect(self.stop_robot)
        layout.addWidget(self.stop_btn)

        self.setLayout(layout)

    def move_forward(self):
        print("Sending Move Forward Command")

    def stop_robot(self):
        print("Sending Stop Command")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HexapodGUI()
    window.show()
    sys.exit(app.exec_())
