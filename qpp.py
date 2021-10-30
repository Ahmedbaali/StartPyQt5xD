from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(400,400,200,200)
    win.setWindowTitle("First app with PyQt5")


    label = QtWidgets.QLabel(win)
    label.setText("Hello World")
    label.move(100,100)

    win.show()
    sys.exit(app.exec_())

window()