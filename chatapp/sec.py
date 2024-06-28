from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from chat_client import check_login
import json

def mssf(): pass
def show_friends(frien):
        layout = QVBoxLayout()
        scroll_area = ff.findChild(QScrollArea, "scrollArea")
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        for friend in data['friends']:
            label = QLabel(friend['name'])
            button = QPushButton(friend['name'])
            button.setObjectName(friend['unid'])
            button.clicked.connect(partial(mssf, friend['unid']))
            scroll_layout.addWidget(label)
            scroll_layout.addWidget(button)
        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(False)

def chat_inter():
    
    with open("data.json","r")as f:
        frien=load(f)
        frien=frien["friends"]
    
    app = QApplication([])
    ff = loadUi("chatapp/interfaces/wajhsa.ui")
    ff.show()
    ff.basrr.clicked.connect(mssf)
    app.exec_()


def login_inter():
    def login():
        user = ff.leu.text()
        passr = ff.lep.text()
        ff.lres.clear()
        if len(user) < 5:
            QMessageBox.critical(ff, "error", "user length <5")
        else:
            print("ok")
            x = check_login(user, passr)
            if x:
                ff.lres.setText("login avec success")
            else:
                ff.lres.setText("ther is no user with this info")

    def clss():
        ff.leu.clear()
        ff.lep.clear()
        ff.lres.clear()
    app = QApplication([])
    ff = loadUi("chatapp/interfaces/login.ui")
    ff.show()
    ff.bas.clicked.connect(login)
    ff.bc.clicked.connect(clss)
    app.exec_()
