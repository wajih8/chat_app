
from requests import post


def get_chat(id1, id2, unid, valid):
    e = dict()
    e[unid] = post("http://localhost:3000/getchat",
                   data={"iduser": id1, "idfien": id2, "validation": valid}).json()
    print(e)


get_chat(157, 13, "e1248a142", "j2l917f2iL56eda946kDlvmFe2")
