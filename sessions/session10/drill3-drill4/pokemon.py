while True:
    engDict = {
        'raichu' : '''raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.''',
        'onix' : '''Onix resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.''',
        'pikachu' : '''Pikachu is an Electric-type Pokémon, which was introduced in Generation I. Pikachu is renowned for being the most well-known and recognizable Pokémon. Over the years, Pikachu has become so popular that it serves as the Pokémon franchise mascot. It is the Version Mascot for the game Pokémon Yellow as well as one of the mascots for its remakes Pokémon: Let's Go, Pikachu! and Let's Go, Eevee!. It is also well known from the anime, where Ash Ketchum, the protagonist, owns a Pikachu. It evolves from Pichu when leveled up with high friendship and evolves into Raichu when exposed to a Thunder Stone. When in Alola, it evolves into its Alolan Forme.'''
    }

    search = input('enter one of these three pokemon to discover their origins: (pikachu, raichu, onix) ')
    if search.isupper():
        print(engDict[search.lower()])
    else:
        print(engDict[search])
    # bổ sung nhập chữ hoa