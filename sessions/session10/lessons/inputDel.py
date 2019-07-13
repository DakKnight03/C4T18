movie = {
    'movieName' : 'Sherlock',
    'rating and review' : 9.1,
}
print(movie)
delete = input("what key do you want to delete? ")
del movie[delete]
print(movie)