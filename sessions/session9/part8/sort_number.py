high_score = [10, 45, 90, 100, 74, 20]
while True:
    high_score.sort(reverse = True)
    for i, score in enumerate(high_score):
        print(i + 1, '.', score)
    new_score = int(input('enter your new high score: '))
    high_score.append(new_score)
    print('high scores:')