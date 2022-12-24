import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLCDNumber, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.but = QPushButton('but', self)
        self.but.resize(300, 70)
        self.but.move(20, 30)
        self.but.clicked.connect(self.click)
        self.but.count = 0


        self.lab = QLabel(self)
        self.lab.setText('лейбл')
        self.lab.move(150, 150)

        self.num = QLCDNumber(self)
        self.num.display(228)
        self.num.move(200, 200)

        self.ET = QLineEdit(self)
        self.ET.move(0, 100)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Первая программа')

    def click(self):
        self.but.setText(f'zxc{self.but.count}')
        self.but.count += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
