import datetime
y = str(datetime.datetime.now())[:10]


def cryptage(uid, user, da):
    s = str(datetime.datetime.now())[11:19]
    x = ord("a")
    while len(user) < 10:
        user += chr(x)
        x += 1

    user2 = ""
    for i in range(len(user)):
        if da[i] == "-":
            user2 += user[i]+"k"
        else:
            user2 += user[i]+da[i]

    chcry = ""
    j = -1
    for i in range(len(user2)):
        if j == len(uid)-1:
            j = -1
        else:
            j += 1
        chcry += crypt(user2[i], uid[j])
    chcry = chcry[:4]+s[:2]+chcry[4:8]+s[3:5]+chcry[8:12]+s[6:]+chcry[12:]
    return (chcry)


def crypt(a, b):
    '''if "0" <= a <= "9":
        x = ord(b) % 10
        if x+ord(a) > ord("9"):
            return chr(x+ord(a)-9)
        else:
            return chr(x+ord(a))

    else:'''
    x = ord(b) % 26
    if x+ord(a) > ord("9") and x+ord(a) < ord("A"):
        return chr(x+ord(a)-9)

    elif x+ord(a.upper()) > ord("Z"):
        return chr(x+ord(a)-26)
    else:
        return chr(x+ord(a))


print(cryptage("e1248a42", "wajih", y))
