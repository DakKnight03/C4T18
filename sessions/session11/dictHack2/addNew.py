shop = {
    'HP' : 20,
    'Dell' : 50,
    'MacBook' : 12,
    'Asus' : 30, 
}
shop['Toshiba'] = 10
print(shop)
addNew = input('add a new brand of computer to the shop: ')
amount = int(input('enter the amount of computer of that brand: '))
shop[addNew] = amount
print(shop)

#update shop
shop['Dell'] += 10
shop['MacBook'] -= 2
print(shop)