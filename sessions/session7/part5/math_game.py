from random import *
while True:
    a = randint(0, 15)
    b = randint(-5, 5)
    c = randint(-1, 1)
    sum_ab = a + b
    result = sum_ab + c
    if b >= 0:
        print(a, "+", b, "=", result)
    else:
        print(a, b, "=", result)
    respond = input("true or false? ")
    if sum_ab == result:
        if respond == "true":
            print("correct")
        elif respond == "false":
            print("incorrect")
            break
        else:
            print("type in true or false")
    else:
        if respond == "false":
            print("correct")
        elif respond == "true":
            print("incorrect")
            break
        else:
            print("type in true or false")
