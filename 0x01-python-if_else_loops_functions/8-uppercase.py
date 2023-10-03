#!/usr/bin/python3
def uppercase(str):
    tmp = list(str)
    for mk in range(len(tmp)):
        if (ord(tmp[mk]) > 96 and ord(tmp[mk]) < 123):
            tmp[mk] = chr(ord(tmp[mk]) - 32)
    print("{}".format(("").join(tmp)))
