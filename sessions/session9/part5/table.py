district = ['ST', 'BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
population = [150300, 247100, 333300, 266800, 420900, 318000]
highest = max(population)
lowest = min(population)
print('highest population =', highest)
print('lowest population =', lowest)
index_high = population.index(highest)
index_low = population.index(lowest)
print('district', district[index_high], 'has the highest population')
print('district', district[index_low], 'has the lowest population')