n = int(input("what is n? "))
if n <= 0:
    print("n must be bigger than 0")
else:
    for i in range(n + 1):
        print(i, end=' ')