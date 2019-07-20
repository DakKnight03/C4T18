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

for n, i in enumerate(skillTree):
    print(n + 1, '.', i['name'])