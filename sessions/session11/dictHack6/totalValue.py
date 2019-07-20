shop = {
    'HP' : 20,
    'Dell' : 50,
    'MacBook' : 12,
    'Asus' : 30,
    'Toshiba' : 10,
    'Fujitsu' : 15,
    'Alienware' : 5,
}
price = {
    'HP' : 600,
    'Dell' : 650,
    'MacBook' : 12000,
    'Asus' : 400,
    'Toshiba' : 600,
    'Fujitsu' : 900,
    'Alienware' : 1000,
}
superTotal = []
l = len(shop)
for k in shop.keys():
    totalValue = shop[k] * price[k]
    print('total value of', k, 'computer is', totalValue)
    superTotal.append(totalValue)
print('total value of all computers:', sum(superTotal))