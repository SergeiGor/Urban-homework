# Форматирование строк

# Использование %:
team1_num = int(input('Введите число участников первой команды: ' ) )
print('В первой команде "Мастера кода" участников: %s ! ' % team1_num)
team2_num = int(input('Введите число участников второй команды: ' ) )
print('Отлично! Итого сегодня в командах участников: %s и %s ! ' % (team1_num, team2_num))

# Использование format():
score_1 = int(input('Введите число решенных задач первой командой: ' ) )
score_2 = int(input('Введите число решенных задач второй командой: ' ) )
print('Первая команда решила задач - {}, вторая - {}'.format(score_1,score_2))

team1_time = 1552.512
team2_time = 2153.31451
print('Вторая команда "Волшебники данных" решила задачи за {} с !'.format(team2_time))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды "Мастера кода"!'
elif score_1 < score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды "Волшебники Данных"!'
else:
    result = 'Ничья!'

challenge_result = f'Результат битвы: {result}'

tasks_total = f'Сегодня было всего решено задач: {score_1 + score_2}, в среднем по {round((team1_time + team2_time)/(score_1 + score_2),1)} секунды на задачу!'

print(tasks_total)
print(challenge_result)