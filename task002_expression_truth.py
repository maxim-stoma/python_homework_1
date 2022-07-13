print('Введи три числа через пробел:')
x, y, z = map(int, input().split())
if not (x or y or z) == (not x and not y and not z):
    print('Получается, что истинно...')
else:
    print('Кажется, что-то пошло не так...')