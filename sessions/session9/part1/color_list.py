color = ['red', 'green', 'blue']
print('our color list:')
while True:
    for i in range(len(color) - 1):
        print(color[i], end=', ') 
    print(color[-1])
    new_color = input('enter a new color: ')
    color.append(new_color)
    print('our new color list:')