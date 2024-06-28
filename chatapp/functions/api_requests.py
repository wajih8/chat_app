from requests import post, get
from pickle import load


def ser_friends(ch):
    x1 = post("http://localhost:3000/serchfriend", data={"name": ch}).json()


def get_friends():
    with open("indenti.dat", "rb")as f:
        e = load(f)
    x1 = post("http://localhost:3000/getAllFriends", data=e).json()
    print(x1["wa"])
