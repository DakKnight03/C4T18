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

print('price for Acer computer:', price['Acer'])

search = input('what brand of computer are you searching for? ')
print('price for', search, 'computer:', price[search])