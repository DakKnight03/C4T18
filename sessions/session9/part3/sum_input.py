num_input = input('enter numbers: ')
number_list = num_input.split(' ')
sum = 0 
i = 0
length = len(number_list)
while i < length:
    sum += int(number_list[i])
    i += 1
print(sum)