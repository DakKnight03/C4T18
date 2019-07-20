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
    'Acer' : 350,
    'Toshiba' : 600,
    'Fujitsu' : 900,
    'Alienware' : 1000,
}

totalValue = 5 * price['Asus']
print(totalValue)

buy = input('what brand of computer wound you like to buy? ')
amount = int(input('how many do you want to buy? '))
totalValue = amount * price[buy]
print('that will cost', totalValue)