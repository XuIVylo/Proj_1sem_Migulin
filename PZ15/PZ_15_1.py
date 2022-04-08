# Для каждого столбца матрицы с четным номером найти сумму ее элементов.

import random

def summa(list):
    sum = 0
    for i in list:
        sum += i
    return sum

a = int(input('Введите количество столбцов: '))
b = int(input('Введите количество строк: '))

matr = [[random.randint(1, 9) for y in range(a)] for x in range(b)]
matr_rev = [[0 for y in range(b)] for x in range(a)]

print('Матрица: ')
for i in matr:
    print(i)

for i in range(len(matr)):
    for c in range(len(matr[0])):
        matr_rev[c][i] = matr[i][c]
# for i in matr_rev:
#     print(i)

print('\n', 'Четные столбцы матрицы: ')
wew = []
for i in range(len(matr_rev)):
    if i % 2 != 0:
        print(matr_rev[i])
        wew.append(summa(matr_rev[i]))
print('Сумма элементов: ', wew)
