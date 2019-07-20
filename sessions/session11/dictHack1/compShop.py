print('computers in store:')
shop = {
    'HP' : 20,
    'Dell' : 50,
    'MacBook' : 12,
    'Asus' : 30, 
}
print(shop)

print('MacBook in store:', shop['MacBook'])

inputSearch = input('what brand of computer do you want? ')
print('there are', shop[inputSearch], 'in store')