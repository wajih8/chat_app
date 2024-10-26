
def cleanmsg(ch):
    if ch[0] == " ":
        ch[1:]
    if ch[-1] != " ":
        ch += " "
    if len(ch) < 70:
        return False, ch, ""
    else:
        ch1 = ch[:70]
        i = 0
        ch = ch[70:]
        while ch1[-1] != " ":
            ch1 += ch[i]
            i += 1
        ch = ch[i-1:]
        if ch[0] == " ":
            ch = ch[1:]

        return True, ch, ch1
