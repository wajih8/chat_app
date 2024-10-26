from pickle import dump
from PyQt5.QtWidgets import *
import chatapp.functions.chat_inte as csa
x = dict()
x["id"] = 125
x["unid"] = "12azd"
x["username"] = "wajih"
x["validation"] = "waijfa"
# csa.chat_inter()
with open("indenti.dat", "wb")as f:
    dump(x, f)
