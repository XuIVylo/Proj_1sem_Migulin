# Составить генератор (yield), который выводит из строки только цифры.

def chis(sr):
    for i in sr:
        if i in '1234567890':
            yield i


# инициализация строки
sr = ('123312asdfgh')

# вывод начального строки
print("До фильтрации в генераторе: " + str(sr))

# вывод только чисел
print("Только четные числа: ", end="")
for i in chis(sr):
    print(i, end="")