movie = {
    'movieName' : 'Sherlock',
    'rating' : 9.1,
}
key = input('enter a key: ')
value = input('enter the value: ')
movie[key] = value
print(movie)
print(movie['movieName'])
print(movie['rating'])