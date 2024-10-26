from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from chatapp.functions.api_requests import get_chat, sends, check_serever, check_serever2
from json import load as lo
from pickle import load as lopi
from functools import partial
from chatapp.functions.frien_inter import sa
from chatapp.functions.clean_msgs import cleanmsg
import time
import threading
sendid = ""
chid, senam = "", ""
time.sleep(0.1)


def get_my_id():
    mygolid = 0
    try:
        with open("indenti.dat", "rb")as f:
            mygolid = lopi(f)
            mygolid = mygolid
    except:
        pass
    return mygolid


bigid = get_my_id()


def verif(ch):
    i = 0
    tes = True
    while tes and i < len(ch):
        tes = "A" <= ch[i].upper(
        ) <= "Z" or "0" <= ch[i] <= "9" or ch[i] == " "
        i += 1
    return tes and ch.find("  ") == -1 and ch[0] != " " and ch[-1] != " "


def chat_inter():
    global app

    def refrech():
        ff2.laff.clear()
        with open("messages.json", "r")as f:
            try:
                mess = lo(f)
                mess = mess[chid]
            except:
                mess = "<end>ther is no chat bettwen you and "+senam
        if "<end>ther" in mess:

            item = QListWidgetItem(mess[5:])
            ff2.laff.addItem(item)
        else:
            k = 0
            for i in mess:
                k += 1
                ch = i["message"]
                item = QListWidgetItem()
                if i["idsender"] == bigid["id"]:
                    tes = True
                    while tes:

                        tes, ch, clean = cleanmsg(ch)
                        item = QListWidgetItem()
                        item.setTextAlignment(Qt.AlignRight)
                        item.setBackground(Qt.GlobalColor(125))
                        item.setText(clean)
                        if tes and clean != "":
                            ff2.laff.addItem(item)

                    item = QListWidgetItem()
                    item.setTextAlignment(Qt.AlignRight)
                    item.setBackground(Qt.GlobalColor(125))
                    item.setText(ch)
                    ff2.laff.addItem(item)
                else:
                    tes = True
                    while tes:
                        tes, ch, clean = cleanmsg(ch)
                        item = QListWidgetItem()

                        item.setBackground(Qt.GlobalColor(225))
                        item.setTextAlignment(Qt.AlignLeft)
                        item.setText(clean)
                        if tes and clean != "":
                            ff2.laff.addItem(item)

                    item = QListWidgetItem()
                    item.setBackground(Qt.GlobalColor(225))
                    item.setTextAlignment(Qt.AlignLeft)
                    item.setText(ch)
                    ff2.laff.addItem(item)
            ff2.laff.setCurrentRow(k+2)

    def absa2():
        while True:

            if app == None:
                break 
            if check_serever2(bigid["id"]):
                pass
            time.sleep(120)

    def absa():
        ma = 0
        while True:

            if app == None:
                break
            if sendid != "" and chid != "":
                pass
                if check_serever(chid):
                    get_chat(bigid["id"], sendid,
                             chid, bigid["validation"])
                    refrech()

            ma += 1
            time.sleep(15)

    def siba():
        ths2 = threading.Thread(target=absa2,)
        ths = threading.Thread(target=absa,)
        ths.start()
        ths2.start()

    def sendmess():
        if sendid == "":
            QMessageBox.information(
                ff2, "you need to select", "select chat SVP")
            return
        ch = ff2.lmsg.text()

        if ch != "" and verif(ch):
            ff2.lmsg.clear()
            sends(ch, bigid["id"], sendid)
            item = QListWidgetItem()
            item.setTextAlignment(Qt.AlignRight)
            item.setBackground(Qt.GlobalColor(125))
            item.setText(ch)
            ff2.laff.addItem(item)

    def logout():
        with open("indenti.dat", "wb"):
            pass
        app.closeAllWindows()

    def mssf(ids):
        global sendid, bigid, chid, senam
        bigid = get_my_id()
        sendid = ids["id"]
        chid = ids["unid"]
        senam = ids["name"]
        ff2.laff.clear()

        if check_serever(ids["unid"]):
            get_chat(bigid["id"], ids["id"], ids["unid"], bigid["validation"])
        refrech()

    def lser():
        ch = ff2.lserch.text()
        if ch == "" or verif(ch) == False or len(ch) > 16:
            QMessageBox.critical(ff2, "error", "user name or id not valid")
        else:
            sa.serfriend(ch, bigid["id"])

    y = 1
    app = QApplication([])
    ff2 = loadUi("chatapp/interfaces/chatapp.ui")
    ff2.setWindowIcon(QIcon("appicon.ico"))
    with open("data.json", "r")as f:
        frien = lo(f)
    try:
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
            btn.clicked.connect(partial(mssf, fien))
            btn.setFixedSize(120, 30)
            btn.move(10, y)
        scar.setWidget(sccon)
    except:
        pass
    ff2.show()
    ff2.menuoptions.setStyleSheet(
        'background-color: rgb(25, 170, 50);')
    ff2.actionLogOut.triggered.connect(logout)
    ff2.bserch.clicked.connect(lser)
    ff2.bsend.clicked.connect(sendmess)

    siba()
    app.exec_()
    app = None
