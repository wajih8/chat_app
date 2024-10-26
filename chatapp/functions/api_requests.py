from requests import post, get
from pickle import load
from pickle import dump as dum
from json import dump, dumps
from json import load as lo
import time


def check_serever2(ids):

    x1 = post("http://localhost:3000/check_reqt",
              data={"ids": ids}).json()
    with open("temp2.json", "w")as f:
        dump(x1, f)
    return x1["wa"] == "true"


def ser_friends(ch, idsa):
    x1 = post("http://localhost:3000/serchfriend",
              data={"name": ch, "ids": idsa}).json()

    with open("temp.json", "w")as f:
        dump(x1, f)


def sends(a, b, c):

    y = post("http://localhost:3000/send_message",
             data={"iduser": b, "idfien": c, "message": a}).json()

    return y["wa"] == "true"


def check_login(a, b):
    y = post("http://localhost:3000/check_login",
             data={"user": a, "password": b}).json()

    if y["wa"] == "true":
        with open("indenti.dat", "wb")as jsk:
            dum(y, jsk)
    return y["wa"] == "true"


def checkcoockie():

    try:
        with open("indenti.dat", "rb")as f:
            file = load(f)

            t = [file["id"], file["uniqueid"],
                 file["username"], file["validation"]]
            del file
            y = post("http://localhost:3000/checkcoockie",
                     data={"id": t[0], "unid": t[1], "username": t[2], "validation": t[3]}).json()
            del t
        return y["wa"] == "true"
    except:

        return False


def send_friend_req(x):
    try:
        with open("indenti.dat", "rb")as f:
            file = load(f)
            t = file["id"]
            del file
            y = post("http://localhost:3000/send_friend_req",
                     data={"idFF": t, "idSF": x["id"], "username": x["name"]}).json()
            del t
        return y["wa"] == "true"
    except:

        return False


def check_serever(x):
    with open("messages.json", "r")as f:
        try:
            t = lo(f)[x]
            t = t[-1]
        except:
            return True
    dus = {"idse": t["idsender"], "idch": t["idchat"],
           "mess": t["message"], "date": t["date"]}

    a = post("http://localhost:3000/check_last_message",
             data=dus).json()
    return a["wa"] == "true"


def get_chat(id1, id2, unid, valid):

    a = post("http://localhost:3000/getchat",
             data={"iduser": id1, "idfien": id2, "validation": valid}).json()["wa"]

    if not ("<err" in a):

        with open("messages.json", "r")as f:
            try:
                s = lo(f)
            except:
                s = {}
        with open("messages.json", "w")as f:
            s[unid] = a
            dump(s, f)


def get_friends():
    with open("indenti.dat", "rb")as f:
        e = load(f)

    e = e["id"]
    print(e)
    time.sleep(1)

    x1 = post("http://localhost:3000/getAllFriends", data={"id": e}).json()
    with open("data.json", "w")as f:
        dump(x1, f)
