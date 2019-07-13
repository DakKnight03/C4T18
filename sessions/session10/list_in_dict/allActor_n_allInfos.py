infos = {
    'name' : 'infinity war',
    'actor' : ['Benedict Cumberbatch', 'Tom Holland', 'Chris Hemsworth', 'Robert Downey, Jr.', 'Chris Evans', 'Chadwick Aaron Boseman'],
    'year' : 2018,
}
list_actor = infos['actor']
l = len(list_actor)
for i in range(l):
    print(list_actor[i])
print()
for k, v in infos.items():
    print(k, ':', v)