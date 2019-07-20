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

#add 50 gold
char['gold'] += 50

#add flintstone
char['backpack'].append('FlintStone')

#add pocket
char['pocket'] = ['MonsterDex', 'Flashlight']
print(char)