#!/usr/bin/python3
for mk in range(10):
    for j in range(mk + 1, 10):
        print("{}".format(str(mk) + str(j)), end="")
        if int(str(mk) + str(j)) < 89:
            print(", ", end="")
print("")

