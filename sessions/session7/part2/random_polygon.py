from turtle import *
n = int(input("number of sides: "))
shape("turtle")
speed(-1)
for i in range(n):
    forward(100)
    left(360 / n)

mainloop()