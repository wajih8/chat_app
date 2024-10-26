from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

from chatapp.functions.api_requests import ser_friends, send_friend_req
from json import load
from functools import partial


def mssf(a):
    send_friend_req(a)


class sa():
    def __init__(self):
        super(sa, self).__init__()

    def serfriend(ch, i):
        global ff
        ser_friends(ch, i)
        with open("temp.json", "r")as f:
            t = load(f)
        if t["Friend_tes"] != 'good':
            QMessageBox.information(
                ff, "problem", "ther is no user with this name")
            return

        ff = loadUi("chatapp/interfaces/friendsaccept.ui")
        ff.setWindowIcon(QIcon("appicon.ico"))
        with open("temp.json", "r")as f:
            frien = load(f)
        frien = t["Friend_ava"]
        scar = ff.findChild(QScrollArea, "sc")
        sccon = QWidget()
        sccon.setFixedSize(260, 50*len(frien)+5)
        for i, fien in enumerate(frien):
            y = i*50+5
            # label
            lab = QLabel(fien["name"], sccon)
            lab.setFixedSize(100, 30)
            if len(fien["name"]) > 8:
                lab.setStyleSheet(
                    'background-color: rgb(255, 170, 0);font: 9pt "MV Boli";border-radius: 8%;')
            else:
                lab.setStyleSheet(
                    'background-color: rgb(255, 170, 0);font: 14pt "MV Boli";border-radius: 8%;')

            lab.move(10, y)
            # button
            btn = QPushButton("send F.REQUEST", sccon)
            btn.setObjectName(fien["unid"])
            btn.clicked.connect(partial(mssf, fien))
            btn.setFixedSize(120, 30)
            btn.move(140, y)
        scar.setWidget(sccon)
        ff.show()
