infos = {
    'name' : 'infinity war',
    'actor' : ['Benedict Cumberbatch', 'Tom Holland', 'Chris Hemsworth'],
    'year' : 2018,
}

infos['genre'] = ['scifi', 'action', 'superhero']
infos['rating'] = 89

infos['actor'] = ['Robert Downey, Jr.', 'Chris Evans', 'Chadwick Aaron Boseman']

for k, v in infos.items():
    print(k, '-', v)

infos['actor'].append('Chris Pratt') #add another actor

for k, v in infos.items():
    print(k, '-', v) 

infos['actor'].pop(0) #remove the first actor

for k, v in infos.items():
    print(k, '-', v) 