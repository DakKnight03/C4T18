acreage = [117.43, 9.224, 43.35, 12.04, 9.96, 10.09]
district = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = [150300, 247100, 333300, 266800, 420900, 318000]
length = len(district)
for i in range(0, length):
    print("Mat do quan", district[i], "la", population[i] / acreage[i])
total_density = 0
i = 0
while i < length:
    total_density += population[i]/acreage[i]
    i += 1
final_result = total_density / length
print('mat do dan cu trung binh la', final_result)
