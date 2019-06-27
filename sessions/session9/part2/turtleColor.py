from turtle import *
colors = ['red', 'green', 'blue']
shape('turtle')
speed(-1)
for i in range(len(colors)):
    color(colors[i])
    forward(100)
mainloop()