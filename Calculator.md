from PyQt5.QtWidgets import *
import sys
import math


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Simple Calculator By sazid")
        self.setGeometry(500, 500, 400, 400)
        self.display = None
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        vbox = QVBoxLayout()

        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setFixedHeight(60)
        self.display.setStyleSheet("font-size: 35px; padding: 10px;")
        vbox.addWidget(self.display)

        # Button
        grid = [["⬅", "Exit", "√", "."],
                ["9", "8", "7", "/"],
                ["6", "5", "4", "*"],
                ["3", "2", "1", "-"],
                ["C", "0", "=", "+"]]

        for row in grid:
            hbox = QHBoxLayout()
            for ch in row:
                button = QPushButton(ch, self)
                button.setStyleSheet("font-size: 15px; padding: 10px;")
                button.clicked.connect(lambda checked, char=ch: self.click_on_button(char))
                hbox.addWidget(button)
            vbox.addLayout(hbox)
        central_widget.setLayout(vbox)

    def click_on_button(self, char):
        if char == "C":
            self.display.clear()
        elif char == "⬅":
            self.display.setText(self.display.text()[:-1])
        elif char == "√":
            try:
                num = float(self.display.text())
                result = math.sqrt(num)
                self.display.setText(str(result))
            except ValueError:
                self.display.setText("Value Error")
        elif char == "=":
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception:
                self.display.setText("Error")
        elif char == "Exit":
            sys.exit()
        else:
            self.display.setText(self.display.text() + char)


def main():
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
