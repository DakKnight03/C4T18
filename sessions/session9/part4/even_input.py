num_input = input('enter numbers: ')
list_num = num_input.split(', ')
# print(list_num)
list_num = list(map(int, list_num))
# print(list_num)
print('all even numbers:')
for i in list_num:
    if i % 2 == 0:
        print(i)