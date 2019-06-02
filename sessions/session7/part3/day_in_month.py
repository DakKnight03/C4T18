month = int(input("enter a month: "))
year = int(input("enter a year: "))
if 1 <= month <= 12:
    if month in (4, 6, 9, 11):
        print("this month has 30 days")
    elif month == 2:
        if year % 4 == 0 and year % 100 != 0:
            print("this month has 29 days")
        else:
            print("this month has 28 days")
    else:
        print("this month has 31 days")
else:
    print("enter a valid month")