import random
while True:
    list_game = ['game', 'youtube', 'movies', 'coding', 'tech', 'pewdiepie', 'jacksepticeye', 'food', 'stuff', 'laptop']
    random_item = random.choice(list_game)
    a = list(random_item)
    random.shuffle(a)
    print("put these letters in the correct order:", *a, sep= ' | ')
    answer = input("write your answer here: ")
    if answer == random_item:
        print("correct!")
    else:
        print("incorrect.")
        break