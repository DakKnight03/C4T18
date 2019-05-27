month = int(input("choose a month "))
if 1 <= month <= 3:
    print("It is spring")
elif month <= 6:
    print("It is summmer")
elif month <= 9:
    print("It is autumn")
elif month <= 12:
    print("It is winter")
else:
    print("error")
