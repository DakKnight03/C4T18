
fav = input("what is your favorite thing? ")
stuff = fav.split(', ')

l = len(stuff)
print('''this is your favorite stuff:''')
for i in range(l):
    print(stuff[i])