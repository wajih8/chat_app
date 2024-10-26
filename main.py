from PyQt5.QtWidgets import *
import chatapp.functions.log_inte as log_inte
import time
import chatapp.functions.chat_inte as csa
import chatapp.functions.reg_inte as rsa
from chatapp.functions.api_requests import get_friends, checkcoockie


def chat():
    get_friends()
    with open("messages.json", "w")as f:
        pass

    csa.chat_inter()


def login():
    return log_inte.login_inter()


def register():
    rsa.chat_inter()
    print("you made it baby")


if "__main__" == __name__:
    x = checkcoockie()

    y = True
    i = 0
    d = i
    while y and i < 3:

        if x:
            chat()
            y = False
        elif d == 5:

            d = register()
        else:

            i += 1
            d = login()

            x = checkcoockie()

        time.sleep(0.1)
