# В матрице найти минимальный элемент в предпоследнем столбце.

import random

a = int(input('Введите количество строк: '))
b = int(input('Введите количество столбцов: '))
matr = [[random.randint(1, 10) for y in range(a)] for x in range(b)]
for i in matr:
    print(i)

n = a-2
wew = [matr[i][n] for i in range(len(matr))]

print('Минимальный элемент предпоследнего столбца: ', min(wew))