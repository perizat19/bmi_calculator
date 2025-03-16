
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt6.QtGui import QFont


class MyWindow(QMainWindow):

    def calculate_bmi(self):
        weight = float(self.weight_line.text())
        height = float(self.height_line.text())
        bmi = weight / (height ** 2)
        self.result.setText(f'Your BMI: {bmi:.1f}')

        if bmi < 18.5:
            self.status.setText('Status: Underweight')
        elif 18.5 < bmi < 25:
            self.status.setText("Status: Normal weight")
        elif 25 < bmi < 30:
            self.status.setText("Status: Overweight")
        else:
            self.status.setText("Status: Obese")

    def clear_action(self):
        self.weight_line.clear()
        self.height_line.clear()

    def help_action(self):
        instruction = ("1. Enter you weight in kg (for example: 55).\n"
                       "2. Enter your height in meters (for example: 1.75).\n"
                       "3. Push the green button.")
        self.instruction.setText(instruction)

    def create_menubar(self):
        menu = self.menuBar()
        file = menu.addMenu('File')
        help = menu.addMenu('Help')

        exit_action = file.addAction('Exit')
        exit_action.triggered.connect(self.close)

        clear_action = file.addAction('Clear')
        clear_action.triggered.connect(self.clear_action)

        help_action = help.addAction('How to use')
        help_action.triggered.connect(self.help_action)

    def __init__(self):

        super().__init__()
        self.setWindowTitle("BMI Calculator")
        self.setFixedSize(400, 300)

        self.weight_label = QLabel('Weight (kg): ', self)
        self.weight_label.setFont(QFont("Arial", 10))
        self.weight_label.move(20, 30)
        self.weight_line = QLineEdit(self)
        self.weight_line.setFont(QFont("Arial", 10))
        self.weight_line.move(20, 60)

        self.height_label = QLabel('Height (m): ', self)
        self.height_label.setFont(QFont("Arial", 10))
        self.height_label.move(20, 90)
        self.height_line = QLineEdit(self)
        self.height_line.move(20, 120)

        self.calc_button = QPushButton(self)
        self.calc_button.setText("Calculate BMI")
        self.calc_button.setFont(QFont("Arial", 10))
        self.calc_button.move(20, 160)
        self.calc_button.setStyleSheet(
            "background-color: #4CAF50; color: white; font-size: 14px; padding: 5px; border-radius: 5px;")

        self.result = QLabel(self)
        self.result.setFont(QFont("Arial", 10))
        self.result.move(20, 200)

        self.status = QLabel(self)
        self.status.setFont(QFont("Arial", 10))
        self.status.setMinimumWidth(500)
        self.status.move(20, 220)

        self.instruction = QLabel(self)
        self.instruction.move(130, 20)
        self.instruction.setMinimumWidth(500)
        self.instruction.setMinimumHeight(100)

        self.calc_button.clicked.connect(self.calculate_bmi)
        self.create_menubar()














