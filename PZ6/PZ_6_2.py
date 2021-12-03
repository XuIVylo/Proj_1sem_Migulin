# Дан список A размера N. Сформировать два новых списка B и C: в список B записать
# все положительные элементы списка A, в список C — все отрицательные (сохраняя
# исходный порядок следования элементов). Вывести вначале размер и содержимое
# списка B, а затем — размер и содержимое списка C.

from random import randint
a = []
n = int(input('Введите размер списка: '))


while n:  # создание рандомного набора чисел в списке
    a.append(randint(-100, 100))
    n -= 1
print('Изначальный список: ', a)
b = [j for i, j in enumerate(a) if j>0] # Создания списка b с только положительными числами
print('Количество положительных чисел:', len(b))
print('Числа: ',b)

c = [j for i, j in enumerate(a) if j<0] # Создания списка c с только отрицательными числами
print('Количество отрицательных чисел:', len(c))
print('Числа: ',c)
