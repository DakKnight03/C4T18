favorite = ['YouTube', 'Coding', 'Insta']
favorite.pop(-2)
remove = 'LOL'
if remove in favorite:
    favorite.remove(remove)
    print(favorite)
else:
    print("not found")