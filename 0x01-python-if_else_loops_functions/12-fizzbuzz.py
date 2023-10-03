#!/usr/bin/python3
def fizzbuzz():
    for mk in range(1, 101):
        if (mk % 15 == 0):
            print("FizzBuzz ", end="")
        elif (mk % 3 == 0):
            print("Fizz ", end="")
        elif (mk % 5 == 0):
            print("Buzz ", end="")
        else:
            print("{:d} ".format(mk), end="")
