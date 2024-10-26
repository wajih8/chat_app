from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
def mssf(): return (5)


def chat_inter():
    global ff3
    app = QApplication([])
    ff3 = loadUi("chatapp/interfaces/register.ui")
    ff3.show()

    ff3.bas.clicked.connect(mssf)
    app.exec_()
    return (0)
