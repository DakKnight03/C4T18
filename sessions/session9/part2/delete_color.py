colors = ['red', 'green', 'blue', 'purple']
print('our color list:')
while True:
    for i, color in enumerate(colors):
        print(i + 1,'.', color)
    delete_color = input('item to delete: ')
    if delete_color.isalpha():
        colors.remove(delete_color)
    elif delete_color.isdigit():
        colors.pop(int(delete_color) - 1)
    print('our new color list:')