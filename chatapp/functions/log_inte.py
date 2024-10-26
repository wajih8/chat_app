from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from chatapp.functions.api_requests import check_login
import time


def verif(ch):
    i = 0
    tes = True
    while tes and i < len(ch):
        tes = "A" <= ch[i].upper(
        ) <= "Z" or "0" <= ch[i] <= "9" or ch[i] == " "
        i += 1
    return tes and ch.find("  ") == -1 and ch[0] != " " and ch[-1] != " "


def login_inter():

    global kls
    kls = "d"

    def login():
        user = ff.leu.text()
        passr = ff.lep.text()
        ff.lres.clear()
        if len(user) < 5:
            QMessageBox.critical(ff, "error", "user length <5")
        else:
            x = check_login(user, passr)

            if x:
                ff.lres.setText("login avec success")
                app.exit()

            else:
                ff.lres.setText("ther is no user with this info")

    def mal():
        global kls
        QMessageBox.information(ff, "mrigla", "wlh mrigla w ti5dim")
        kls = "s"
        app.exit()

    def clss():
        ff.leu.clear()
        ff.lep.clear()
        ff.lres.clear()
    app = QApplication([])
    ff = loadUi("chatapp/interfaces/login.ui")
    ff.show()
    ff.rejes.triggered.connect(mal)
    ff.bas.clicked.connect(login)
    ff.bc.clicked.connect(clss)
    app.exec_()
    ff.hide()
    if kls == "s":
        return (5)
    else:
        return 0
