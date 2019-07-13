test = {
    'question' : ['1. choose the correct answer:', '2. how many legs does a horse have?', '3. which the highest resolution?'],
    'A' : ['1 + 1 = 3', 6, '4k'],
    'B' : ['14 + 30 = 44', 2, '144p'],
    'C' : ['1 * 0 = 10', 4, '360p'],
    'D' : ['100000009080898 * 346346 - 1534896 / 242356 + 9 * 0 = 4658934534768934', 0, '1080p'],
}
correct_answer = ['B', 'C', 'A']

l = len(test['question'])
x = 0
for i in range(l):
    for k, v in test.items():
        print(k, ':', v[i])
    answer = input('answer: ')
    if answer == correct_answer[i] or answer == correct_answer[i].lower():
        print('correct!')
        x += 1
    else:
        print('false!')
print('you have answered correctly:', x, 'questions!')
percentage = (x / l) * 100
print('correct answer percentage:', percentage, '% !!!')