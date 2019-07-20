var = input('import to random.txt: ')
with open("random.txt", "a") as out:
    out.write(var + '\n')