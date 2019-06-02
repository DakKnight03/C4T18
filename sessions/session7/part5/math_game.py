from random import *
while True:
    a = randint(0, 15)
    b = randint(-5, 5)
    c = randint(-2, 2)
    sum_ab = a + b
    result = sum_ab + c
    print(a, "+", b, "=", result)
    respond = input("true or false? ")
    if sum_ab == result:
        if respond == "true":
            print("correct")
        elif respond == "false":
            print("incorrect")
        else:
            print("type in true or false")
    else:
        if respond == "false":
            print("correct")
        elif respond == "true":
            print("incorrect")
        else:
            print("type in true or false")