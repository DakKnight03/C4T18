random_num = [1, 2, 10, 5, 6, 26, 3, -30]
#use sum()
sum_num = sum(random_num)
print('the sum of all random number in list is', sum_num)
#don't use sum()
sum = 0
i = 0
while i < len(random_num):
    sum += random_num[i]
    i += 1

print(sum)