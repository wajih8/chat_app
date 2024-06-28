from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from chatapp.functions.api_requests import ser_friends
from json import load as lo
from functools import partial


def verif(ch):
    i = 0
    tes = True
    while tes and i < len(ch):
        tes = "A" <= ch[i].upper(
        ) <= "Z" or "0" <= ch[i] <= "9" or ch[i] == " "
        i += 1
    return tes and ch.find("  ") == -1 and ch[0] != " " and ch[-1] != " "


def mssf(a):
    print(a)


def chat_inter():
    def lser():
        ch = ff2.lserch.text()
        if ch == "" or verif(ch) == False or len(ch) > 16:
            QMessageBox.critical(ff2, "error", "user name or id not valid")
        else:
            data = ser_friends(ch)
            x = QMessageBox()
            x.show()
            x.setText("ti bara rawah")
            x.setFixedSize(500, 600)
            x.exec_()

    y = 1
    app = QApplication([])
    ff2 = loadUi("chatapp/interfaces/chatapp.ui")
    ff2.setWindowIcon(QIcon("appicon.ico"))
    with open("data.json", "r")as f:
        frien = lo(f)
    frien = frien["friends"]
    scar = ff2.findChild(QScrollArea, "scrollArea")
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

        lab.move(140, y)
        # button

        btn = QPushButton("Chat with", sccon)
        btn.setObjectName(fien["unid"])
        btn.clicked.connect(partial(mssf, fien["name"]))
        btn.setFixedSize(120, 30)
        btn.move(10, y)
    scar.setWidget(sccon)
    ff2.show()

    ff2.menuoptions.setStyleSheet(
        'background-color: rgb(25, 170, 50);')
    for i in range(10):
        item = QListWidgetItem("wajih")
        if i % 2 == 0:
            item.setTextAlignment(Qt.AlignRight)
        else:
            item.setTextAlignment(Qt.AlignLeft)
        ff2.laff.addItem(item)
    ff2.bserch.clicked.connect(lser)
    ff2.bsend.clicked.connect(mssf)
    app.exec_()
