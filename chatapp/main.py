
from PyQt5.QtWidgets import *
import sec
from pickle import load, dump
from chat_client import checkcoockie


def chat():
    sec.chat_inter()


def login():
    sec.login_inter()


if "__main__" == __name__:
    if checkcoockie():
        chat()
    else:
        login()
