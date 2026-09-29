import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QGridLayout, QLineEdit, QPushButton,
    QMessageBox
)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(300, 400)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 25px;")

        main_layout.addWidget(self.display)

        grid = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('⌫', 4, 0), ('.', 4, 1)
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 20px;")

            button.clicked.connect(lambda checked, value=text: self.handle_button(value))

            grid.addWidget(button, row, col)

        main_layout.addLayout(grid)

        self.setLayout(main_layout)

    def handle_button(self, value):
        if value == 'C':
            self.display.clear()

        elif value == '⌫':
            self.display.backspace()

        elif value == '=':
            self.calculate()

        else:
            self.display.setText(self.display.text() + value)

    def calculate(self):
        expression = self.display.text()

        if expression == "":
            QMessageBox.warning(self,"Lỗi","Bạn chưa nhập biểu thức")
            return

        try:
            result = eval(expression)
            self.display.setText(str(result))

        except ZeroDivisionError:
            QMessageBox.warning(self,"Lỗi","Không thể chia cho 0")

        except Exception:
            QMessageBox.warning(self,"Lỗi","Biểu thức không hợp lệ")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    calculator = Calculator()

    calculator.show()

    sys.exit(app.exec_())