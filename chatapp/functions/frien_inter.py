def verif(ch):
    i = 0
    tes = True
    while tes and i < len(ch):
        tes = "A" <= ch[i].upper(
        ) <= "Z" or "0" <= ch[i] <= "9" or ch[i] == " "
        i += 1
    return tes and ch.find("  ") == -1 and ch[0] != " " and ch[-1] != " "
