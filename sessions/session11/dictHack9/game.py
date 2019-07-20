from random import *
char = {
    'name' : 'Light',
    'age' : 17,
    'strength' : 8,
    'defense' : 10,
    'hp' : 100,
    'backpack' : ['Shield', 'Bread Loaf'],
    'gold' : 100,
    'level' : 2,
}

skill1 = {
    'name' : 'Tackle',
    'minimum level' : 1,
    'damage' : 5,
    'hit rate' : 0.3,
}

skill2 = {
    'name' : 'Quick Attack',
    'minimum level' : 2,
    'damage' : 3,
    'hit rate' : 0.5,
}

skill3 = {
    'name' : 'Strong Kick',
    'minimum level' : 4,
    'damage' : 9,
    'hit rate' : 0.2,
}

skillTree = [skill1, skill2, skill3]
while True:
    hitRate = uniform(0, 1)
    print('BeastMaster69 approached you! Do something!')
    print('choose a skill!')
    for n, i in enumerate(skillTree):
        print(n + 1, '.', i['name'])
    choose = int(input('enter skill number!!! '))
    if char['level'] >= skillTree[choose - 1]['minimum level']:
        if hitRate >= skillTree[choose - 1]['hit rate']:
            print('successful hit!')
            print('BeastMaster69 received', skillTree[choose - 1]['damage'], 'damage!!!')
            print('he fockin ded!!!')
            break
        else:
            print('you missed!')
    else:
        print('your level is too low to activate thsi skill!')