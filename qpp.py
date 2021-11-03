from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class TestWindow(QMainWindow):
    def __init__(self):
        super(TestWindow, self).__init__()
        self.setGeometry(400,400,200,200)
        self.setWindowTitle("First app with PyQt5")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Hello World")
        self.label.move(80,80)    

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me!")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("The button is clicked!!")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = TestWindow()
    win.show()
    sys.exit(app.exec_())

window()