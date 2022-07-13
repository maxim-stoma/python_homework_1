print('Введи номер дня недели: ')
day_number = int(input())
if day_number <= 0:
    print(f'Ты серьёзно? {day_number}-й номер дня недели?')
elif day_number > 7:
    print(f'Ну и где ты видел {day_number} дней недели, умник?')
elif 0 < day_number < 6:
    print('Будний день...работай, солнце ещё высоко.')
else:
    print('Кайфуй, выходные же.')