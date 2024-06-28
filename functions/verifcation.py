from pickle import load, dump
import sqlite3 as sql


def rowcount(rows):
    t = []
    i = 0
    for row in rows:
        t.append(row)
        i += 1
    return i, t


def verifcation_exist(a):
    tes = False
    with open(a, "rb")as f:
        try:
            e = load(f)
            ids = e["id"]
            uids = e["uniqueid"]

            with sql.connect("database/appdb.db")as db:
                cu = db.cursor()
                res = cu.execute(
                    f"select * from users where id={ids} and unid='{uids}' ")
                i, t = rowcount(res)
                if i == 1:
                    if t[0][0] == ids and uids == t[0][1] and e["username"].upper() == t[0][2].upper():
                        tes = True
        except:
            pass
    return tes
