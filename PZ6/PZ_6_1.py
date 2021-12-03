# Дан список A размера N. Вывести вначале его элементы с четными номерами (в
# порядке возрастания номеров), а затем — элементы с нечетными номерами (также в
# порядке возрастания номеров): A2, A4, А6, . . ., A1, A3, A5, ... . Условный оператор не
# использовать.

from random import randint
a = []
n = int(input('Введите размер списка: '))


while n:  # создание рандомного списка
    a.append(randint(0, 100))
    n -= 1
print('Изначальный список: ', a)

print("Чётные:")
print(a[1::2])

print("Нечётные:")

a2 = [j for i, j in enumerate(a) if i%2 == 0]  # присваивание значений с нечётными номерами
print(a2[::1])