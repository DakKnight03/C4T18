random_num = [1, 2, 10, 5, 6, 26, 3]
enter_num = int(input('enter a number: '))
if enter_num in random_num:
    print('found, position', enter_num)
else:
    print('not found in our list')