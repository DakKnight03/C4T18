from random import *


#character infos
name = input('enter your name: ')
strength = 8
defense = 10
hp = 100
level = 2
equipment = []


#level. 0 escape means level 1
escape = 0


#pass 6 levels with hp > 0 to win
while escape < 6 and hp > 0:
    if hp <= 0:
        print('you failed to escape')
        break


    #the map
    map = [
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ['_', '_', '_', '_', '_', '_', '_'],
        ]
    h = len(map)


    #player's coordinations
    px = 0
    py = 0


    #exit's coordinations
    ex = 0
    ey = 0


    #key 1's coordinations
    kx = randint(0, h - 1)
    ky = randint(0, h - 1)


    #no double coordinations
    while px == ex and py == ey or px == kx and py == ky:
        px = randint(0, h - 1)
        py = randint(0, h - 1)
    while ex == kx and ey == ky or ex == px and ey == py:
        ex = randint(0, h - 1)
        ey = randint(0, h - 1)

    
    #replace coordinations with exit and key
    map[ex][ey] = 'e'
    map[kx][ky] = 'k'


    #wall coordinations
    wx = range(randint(0, 3), 6)
    wy = randint(2, 5)

    for i in wx:
        while i == px and wy == py or i == ex and wy == ey or i == kx and wy == ky:
            wx = range(randint(0, 3), 6)
            wy = randint(2, 5)
    for i in wx:
        map[i][wy] = 'w'


    #enter level 2
    if escape >= 1:


        #key 2's coordinations
        kx2 = randint(0, h - 1)
        ky2 = randint(0, h - 1)


        #no double coordinations
        while kx2 == ex and ky2 == ey or kx2 == px and ky2 == py or kx2 == kx and ky2 == ky:
            kx2 = randint(0, h - 1)
            ky2 = randint(0, h - 1)
        map[kx2][ky2] = 'k2'


        # wx = range(randint(0, 3), randint(4, 6))
        # wy = randint(2, 5)

        for i in wx:
            while i == px and wy == py or i == ex and wy == ey or i == kx and wy == ky or i == kx2 and wy == ky2:
                wx = range(randint(0, 3), 6)
                wy = randint(2, 5)
        for i in wx:
            map[i][wy] = 'w'


    #enter level 3
    if escape >= 2:
        char = {
            'name' : name,
            'strength' : strength,
            'defense' : defense,
            'hp' : hp,
            'equipment' : [],
            'level' : level,
        }


        #monster's coordinations
        mx = randint(0, h - 1)
        my = randint(0, h - 1)

        while mx == ex and my == ey or mx == px and my == py or mx == kx and my == ky or mx == kx2 and my == ky2:
            mx = randint(0, h - 1)
            my = randint(0, h - 1)
        map[mx][my] = 'm'


        #character info chart
        # char = {
        #     'name' : name,
        #     'strength' : strength,
        #     'defense' : defense,
        #     'hp' : hp,
        #     'equipment' : [],
        #     'level' : level,
        # }


        #skill infos
        skill1 = {
            'name' : 'Tackle',
            'minimum level' : 1,
            'damage' : 5,
            'hit rate' : 0.3,
        }

        skill2 = {
            'name' : 'Quick Attack',
            'minimum level' : 3,
            'damage' : 3,
            'hit rate' : 0.5,
        }

        skill3 = {
            'name' : 'Strong Kick',
            'minimum level' : 5,
            'damage' : 9,
            'hit rate' : 0.2,
        }

        skillTree = [skill1, skill2, skill3]


        #warning when enter level 3 (and above)
        print('now monsters will appear. Be careful!')
        print('here is your character stats')
        for k, v in char.items():
            print(k, ':', v)
    

    #level 4
    if escape >= 3:
        print('there are hidden hp bars under the dirt. Make sure to find them to regain 10 hp!')


        #hp coordinations
        hx = randint(0, h - 1)
        hy = randint(0, h - 1)

        for i in wx:
            while hx == px and hy == py or hx == ex and hy == ey or hx == kx and hy == ky or hx == kx2 and hy == ky2 or hx == mx and hy == my or hx == i and hy == wy:
                hx = randint(0, h - 1)
                hy = randint(0, h - 1)


    #player's keys
    key = 0
    hp_received = 0


    #level 5
    if escape >= 4:
        print('there are helmets, armors and swords now. Make sure to pick them up to increase you strength and defense')
        ax = randint(0, h - 1)
        ay = randint(0, h - 1)
        helx = randint(0, h - 1)
        hely = randint(0, h - 1)
        sx = randint(0, h - 1)
        sy = randint(0, h - 1)
        for i in wx:
            while ax == px and ay == py or ax == ex and ay == ey or ax == kx and ay == ky or ax == kx2 and ay == ky2 or ax == mx and ay == my or ax == hx and ay == hy or ax == helx and ay == hely or ax == sx and ay == sy or ax == i and ay == wy:
                ax = randint(0, h - 1)
                ay = randint(0, h - 1)
            while helx == px and hely == py or helx == ex and hely == ey or helx == kx and hely == ky or helx == kx2 and hely == ky2 or helx == i and hely == wy or helx == mx and hely == my or helx == hx and hely == hy or helx == sx and hely == sy:
                helx = randint(0, h - 1)
                hely = randint(0, h - 1)
            while sx == px and sy == py or sx == ex and sy == ey or sx == kx and sy == ky or sx == kx2 and sy == ky2 or sx == i and sy == wy or sx == mx and sy == my or sx == hx and sy == hy:
                sx = randint(0, h - 1)
                sy = randint(0, h - 1)

        
        map[ax][ay] = 'a'
        map[helx][hely] = 'h'
        map[sx][sy] = 's'

        


    #the game
    while True:
        print('level', escape + 1 )
        print('you have', key, 'key')
        map[px][py] = 'p'


        #print the map
        for i in map:
            print(*i)


        #the controls
        control = input('enter your control (w, a, s, d) ')
        if control == 'w':


            #cant go up if hit wall or go to exit without key
            if px == 0 or px == ex + 1 and py == ey and key < 1 or escape >= 1 and px == ex + 1 and py == ey and key < 2 or map[px - 1][py] == 'w':
                print('invalid move')
            else:
                map[px][py] = '_'
                px -= 1

        if control == 's':


            #cant go down if hit wall or go to exit without key
            if px == h - 1 or px == ex - 1 and py == ey and key < 1 or escape >= 1 and px == ex - 1 and py == ey and key < 2 or map[px + 1][py] == 'w':
                print('invalid move')
            else:
                map[px][py] = '_'
                px += 1

        if control == 'a':


            #cant go left if hit wall or go to exit without key
            if py == 0 or py == ey + 1 and px == ex and key < 1 or escape >= 1 and py == ey + 1 and px == ex and key < 2 or map[px][py - 1] == 'w':
                print('invalid move')
            else:
                map[px][py] = '_'
                py -= 1

        if control == 'd':


            #cant go right if hit wall or go to exit without key
            if py == h - 1 or py == ey - 1 and px == ex and key < 1 or escape >= 1 and py == ey - 1 and px == ex and key < 2 or map[px][py + 1] == 'w':
                print('invalid move')
            else:
                map[px][py] = '_'
                py += 1


        #if in level 1
        if escape == 0:


            #take key 1
            if map[kx][ky] == 'k':
                if px == kx and py == ky:
                    print('key received')
                    key += 1


            #when have enough keys
            if key == 1:
                if px == ex and py == ey:
                    print('escaped!')
                    escape += 1
                    break
            elif key == 0:
                print('take key first')


        #when in level 2
        if escape >= 1:


            #take key 2
            if map[kx2][ky2] == 'k2':
                if px == kx2 and py == ky2:
                    print('key received')
                    key += 1


            #take key 1
            if map[kx][ky] == 'k':
                if px == kx and py == ky:
                    print('key received')
                    key += 1


            #when have enough keys
            if key == 2:
                if px == ex and py == ey:
                    print('escaped!')
                    escape += 1
                    break


        #when in level 3 (and above)
        if escape >= 2:


            #when near monster
            if px == mx and py == my + 1 or py + 1 == my and px == mx or py == my and mx + 1 == px or py == my and px + 1 == mx:
                if map[mx][my] == 'm':
                    for k, v in char.items():
                        print(k, ':', v)


                    # monster info
                    mon = {
                        'name' : 'BeastMaster64',
                        'strength' : randint(5, 30),
                        'hp' : randint(10, 40),
                        'defense' : randint(2, 30),
                    }

                    print(mon['name'], "'s hp:", mon['hp'])
                    print(mon['name'], "'s defense:", mon['defense'])
                    print(mon['name'], "'s strength:", mon['strength'])
                    print()

                    #choose attack, run or defense
                    choosePlan = input('a monster approached you! What will you do? (run, attack, defense) ')
                    print()

                    #attack
                    if choosePlan == 'attack':


                        #player's turn
                        while mon['hp'] > 0 and hp > 0:
                            print(mon['name'], "'s hp:", mon['hp'])
                            print(mon['name'], "'s defense:", mon['defense'])
                            print(mon['name'], "'s strength:", mon['strength'])
                            print()
                            # if mon['defense'] <= 0:
                            #     print(mon['name'], "'s hp:", mon['hp'])
                            #     print(mon['name'], 'have 0 defense!')
                            print('choose a skill! ')
                            print()
                            for n, i in enumerate(skillTree):
                                print(n + 1, '.', i)
                                print()
                            choose = input('enter skill number!!! ')
                            if choose == '1' or choose == '2' or choose == '3':
                                dam = skillTree[int(choose) - 1]['damage'] + char['strength']
                            if char['level'] >= skillTree[int(choose) - 1]['minimum level']:
                                hitRate = uniform(0, 1)


                                #if player successfully hit the monster
                                if hitRate <= skillTree[int(choose) - 1]['hit rate']:
                                    print('successful hit!')
                                    print('you dealt', dam, 'damage!')
                                    print()
                                    received_dam = dam - mon['defense']
                                    if dam >= mon['defense']:
                                        mon['hp'] -= received_dam
                                        print(mon['name'], 'received', received_dam, 'damage')
                                    else:
                                        print("you dealt 0 damage because the monster's defense is higher than you strength")
                                        print()

                                # if mon['defense'] <= 0:
                                #     mon['hp'] += received_dam
                                    if mon['hp'] <= 0:
                                            map[mx][my] = '_'
                                            level += 1
                                            print(mon['name'], 'is dead! You have leveled up to level', level)


                                #monster's turn
                                    elif mon['hp'] > 0 or hitRate > skillTree[int(choose) - 1]['hit rate']:
                                        print('you missed!')
                                        print()


                                    #monster attack
                                        print(mon['name'], 'attacked you')
                                        print()
                                        crit = uniform(0, 1)
                                        if crit >= 0.7:
                                            print('critical hit!')
                                            def_dam = mon['strength'] * 2 - defense
                                            # defense -= mon['strength'] * 2
                                            print(mon['name'], 'dealt', mon['strength'] * 2, 'damage!')
                                            if mon['strength'] * 2 >= defense:
                                                hp -= def_dam
                                                print('you received', def_dam, 'damage!')
                                            else:
                                                print("you received 0 damage because you defense is higher than the monster's strength")
                                                print()
                                            if hp <= 0:
                                                print('you are dead!')
                                                break

                                        else:
                                            def_dam = mon['strength'] - defense
                                            print(mon['name'], 'dealed', mon['strength'], 'damage!')
                                            if mon['strength'] >= defense:
                                                hp -= def_dam
                                                print('you received', def_dam, 'damage!')
                                            else:
                                                print("you received 0 damage because you defense is higher than the monster's strength")
                                                print()
                                                print('you have', defense, 'defense')
                                                print('you have', hp, 'hp')

                                #level too low to activate skill
                            else:
                                print('your level is too low to activate this skill!')
                                print()


                    #run
                    elif choosePlan == 'run' or choose == 'run':
                        chances = uniform(0, 1)
                        successRate = uniform(0.2, 0.7)


                        #if player successfully ran away
                        if chances <= successRate:
                            print('you ran away!')


                        #if player failed to run away
                        else:
                            print('you failed to run away!')
                            print('you have to fight!')


                                        #monster attack
                            print(mon['name'], 'attacked you')
                            print()
                            crit = uniform(0, 1)
                            if crit >= 0.7:
                                print('critical hit!')
                                def_dam = mon['strength'] * 2 - defense
                                print(mon['name'], 'dealed', mon['strength'] * 2, 'damage!')
                                # defense -= mon['strength'] * 2
                                if mon['strength'] * 2 >= defense:
                                    hp -= def_dam
                                    print(mon['name'], 'dealt', def_dam, 'damage!')
                                else:
                                    print("you received 0 damage because you defense is higher than the monster's strength")
                                    print()
                                if hp <= 0:
                                    print('you are dead!')
                                    break

                            else:
                                def_dam = mon['strength'] - defense
                                print(mon['name'], 'dealed', mon['strength'], 'damage!')
                                if mon['strength'] >= defense:
                                    hp -= def_dam
                                    print(mon['name'], 'dealed', def_dam, 'damage!')
                                else:
                                    print("you received 0 damage because you defense is higher than the monster's strength")
                                    print()
                                    print('you have', defense, 'defense')
                                    print('you have', hp, 'hp')


                            #player's turn
                            while mon['hp'] > 0 and hp > 0:
                                print(mon['name'], "'s hp:", mon['hp'])
                                print(mon['name'], "'s defense:", mon['defense'])
                                print(mon['name'], "'s strength:", mon['strength'])
                                # if mon['defense'] <= 0:
                                #     print(mon['name'], "'s hp:", mon['hp'])
                                #     print(mon['name'], 'have 0 defense!')
                                print('choose a skill! ')
                                for n, i in enumerate(skillTree):
                                    print(n + 1, '.', i)
                                choose = input('enter skill number!!! ')
                                if choose == '1' or choose == '2' or choose == '3':
                                    dam = skillTree[int(choose) - 1]['damage'] + char['strength']
                                if char['level'] >= skillTree[int(choose) - 1]['minimum level']:
                                    hitRate = uniform(0, 1)


                                    #if player successfully hit the monster
                                    if hitRate <= skillTree[int(choose) - 1]['hit rate']:
                                        print('successful hit!')
                                        received_dam = dam - mon['defense']
                                        print('you dealt', dam, 'damage!')
                                        if dam >= mon['defense']:
                                            mon['hp'] -= received_dam
                                            print(mon['name'], 'received', received_dam, 'damage!!!')
                                        else:
                                            print("you dealt 0 damage because the monster's defense is higher than you strength")
                                            print()

                                    # if mon['defense'] <= 0:
                                    #     mon['hp'] += received_dam
                                        if mon['hp'] <= 0:
                                                map[mx][my] = '_'
                                                level += 1
                                                print(mon['name'], 'is dead! You have leveled up to level', level)


                                    #monster's turn
                                        elif mon['hp'] > 0 or hitRate > skillTree[int(choose) - 1]['hit rate']:
                                            #if player missed
                                            print('you missed!')
                                            print()


                                        #monster attack
                                            print(mon['name'], 'attacked you')
                                            print()
                                            crit = uniform(0, 1)
                                            if crit >= 0.7:
                                                print('critical hit!')
                                                def_dam = mon['strength'] * 2 - defense
                                                print(mon['name'], 'dealed', mon['strength'] * 2, 'damage!')
                                                # defense -= mon['strength'] * 2
                                                if mon['strength'] * 2 >= defense:
                                                    hp -= def_dam
                                                    print(mon['name'], 'dealt', def_dam, 'damage!')
                                                else:
                                                    print("you received 0 damage because you defense is higher than the monster's strength")
                                                    print()
                                                if hp <= 0:
                                                    print('you are dead!')
                                                    break

                                            else:
                                                def_dam = mon['strength'] - defense
                                                print(mon['name'], 'dealed', mon['strength'], 'damage!')
                                                if mon['strength'] >= defense:
                                                    hp -= def_dam
                                                    print('you received', def_dam, 'damage!')
                                                else:
                                                    print("you received 0 damage because you defense is higher than the monster's strength")
                                                    print()
                                                    print('you have', defense, 'defense')
                                                    print('you have', hp, 'hp')

                                    #level too low to activate skill
                                else:
                                    print('your level is too low to activate this skill!')
                                    print()


        if escape >= 3:
            if px == hx and py == hy:
                if hp_received == 0:
                    print('you picked up a hp bar hidden under the dirt!')
                    hp += 10
                    print('your hp is increased by 10')
                    hp_received += 1


        if escape >= 4:
            if px == ax and py == ay:
                if map[ax][ay] == 'a':
                    print('you picked up an armor! Your defense is increased by 15')
                    defense += 15

            if px == helx and py == hely:
                if map[helx][hely] == 'h':
                    print('you picked up a helmet! Your defense is increased by 10')
                    defense += 10

            if px == sx and py == sy:
                if map[sx][sy] == 's':
                    print('you picked up a sword! Your strength is increased by 10')
                    strength += 10
        





#winning the game
print('you have won the game!!!')