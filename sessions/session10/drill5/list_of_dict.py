Huy = {
    'name' : 'Huy',
    'role' : 'waiter',
    'hour' : 12,
    'salery' : 0.8,
}

Tung = {
    'name' : 'Tung',
    'role' : 'cook',
    'hour' : 24,
    'salery' : 1.5,
}

Duc = {
    'name' : 'M.Duc',
    'role' : 'manager',
    'hour' : 20,
    'salery' : 2.0,
}

saleryList = [Huy, Tung, Duc]

for i in range(len(saleryList)):
    print(saleryList[i])
    print()

Don = {
    'name' : 'Don',
    'role' : 'waiter',
    'hour' : 12,
    'salery' : 0.9,
}

Hduc = {
    'name' : 'H.Duc',
    'role' : 'waiter',
    'hour' : 14,
    'salery' : 0.7,
}

new_employee = [Don, Hduc]

saleryList.extend(new_employee)

for i in range(len(saleryList)):
    print(saleryList[i])
    print()