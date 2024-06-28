from pickle import load
x = "0x80"
print(int(x, 16))
with open("indenti.dat", "rb")as f:
    print(load(f))
