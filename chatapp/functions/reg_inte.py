from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
def mssf(): pass


def chat_inter():
    app = QApplication([])
    ff2 = loadUi("chatapp/interfaces/register.ui")
    ff2.show()
    # ff2.basrr.clicked.connect(mssf)
    app.exec_()
