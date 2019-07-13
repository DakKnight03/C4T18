p1 = {
    'name' : 'Huy',
    'role' : 'waiter',
    'hour' : 12,
    'salery' : 0.8,
}

p2 = {
    'name' : 'Tung',
    'role' : 'cook',
    'hour' : 24,
    'salery' : 1.5,
}

p3 = {
    'name' : 'M.Duc',
    'role' : 'manager',
    'hour' : 20,
    'salery' : 2.0,
}

saleryList = [p1, p2, p3]

sum = 0
for i in range(len(saleryList)):
    sum += saleryList[i]['hour'] * saleryList[i]['salery'] * 4
    i += 1
print('the company have to spend', sum, 'to pay the employees')