favorite = ['YouTube', 'Coding', 'Insta']
favorite.append('Tokyo')
favorite.append('Game')
favorite.append('Macbook')
# for i in range(6):
#     print(favorite[i].upper())

for i, item in enumerate(favorite):
    print(i, item.upper(), sep='. ')

