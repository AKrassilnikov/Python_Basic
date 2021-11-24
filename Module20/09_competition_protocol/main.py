
def summ(a):
    score = str(a[1][0])
    sum_nums = [int(score[num]) for num in range(len(score))]
    return sum(sum_nums)

score_table = {}
number_rows = int(input('Общее количество строк протокола: '))
print('Введите результат - имя участника (через пробел)')
for time in range(number_rows):
    ball, name = input('{} запись: '.format(time + 1)).split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]
scores = list(score_table.items())
scores.sort(key=summ,reverse = True)
print('\nИтоги соревнований: ')
for winner_index in 0, 1, 2:
    print(f' { winner_index + 1 } место { scores[winner_index][0] } ', end=' ')
    print(f'( { scores[winner_index][1][0] } )', sep='')






