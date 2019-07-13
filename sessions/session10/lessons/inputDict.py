dictionary = {}
while True:
    valueAndKey = input('enter the value and key: (key : value) (enter "done" if done) ')
    if valueAndKey == 'done':
        break
    else:
        list_value = valueAndKey.split(' : ')
        dictionary[list_value[0]] = list_value[1]
        print(dictionary)