from random import randint
number = randint(0, 100)
if number < 30:
    print("Rainy")
elif number < 60:
    print("Cloudy")
else:
    print("Sunny")