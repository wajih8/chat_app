from socket import *
import time
from json import loads
from pickle import dump
discp = "!disco".encode("utf-8")
discp += b" "*(64-6)
add = ('169.254.157.169', 6030)


def check_login(a, b):
    x = ""
    client = socket(AF_INET, SOCK_STREAM)
    while True:
        try:
            client.connect(add)
            break
        except:
            print("can't connect")
            time.sleep(5)

    ta = "login|".encode("utf-8")
    client.send(ta)
    time.sleep(0.12)
    pa = a+'|*|'+b
    client.send(pa.encode("utf-8"))
    time.sleep(3)
    client.send(discp)
    time.sleep(0.5)
    x = client.recv(2048).decode("utf-8")

    if x[:5] == "valid":
        y = loads(x[5:])
        x = x[:5]
        print(x, y)
        with open("indenti.dat", "wb")as jsk:
            dump(y, jsk)

    time.sleep(0.1)
    return x == "valid"


def checkcoockie():

    client = socket(AF_INET, SOCK_STREAM)

    x = ""
    try:
        with open("indenti.dat", "rb")as f:
            while True:
                try:
                    client.connect(add)
                    break
                except:
                    print("can't connect")
                    time.sleep(5)

            file = f.read()
            b = "verlogin|"
            a = "verlogin|".encode("utf-8")
            a += b" "*(64-len(b))

            client.send(a)
            client.send(file)
            time.sleep(3)
            client.send(discp)
            time.sleep(5)
            x = client.recv(30).decode("utf-8")
        return x == "valid"
    except:
        return False
