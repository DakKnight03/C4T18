import random
chosen_word = input("choose a word: ")
jumbled_chosen_word = list(chosen_word)
random.shuffle(jumbled_chosen_word)
l = len(jumbled_chosen_word)
print("jumbled word of", chosen_word)
for i in range(l):
    print(jumbled_chosen_word[i].upper())
