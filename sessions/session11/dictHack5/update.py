shop = {
    'HP' : 20,
    'Dell' : 50,
    'MacBook' : 12,
    'Asus' : 30, 
}

shop['Toshiba'] = 10
shop['Dell'] += 10
shop["MacBook"] -= 2
shop['Fujitsu'] = 15
shop['Alienware'] = 5
extract = input('enter what brand and amount of computer in this format: brand:amount ')
newExtract = extract.split(':')
shop[newExtract[0]] -= int(newExtract[-1])
print(shop)