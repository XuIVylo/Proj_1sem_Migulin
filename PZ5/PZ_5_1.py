# С помощью функций получить вертикальную и горизонтальную линии.
# Линия проводится многократной печатью символа.
# Заключить слово в рамку из полученных линий.

# Создание из символа горизонтальной линии
def hLine(count):
    return '-' * (count + 4)


# Создание двух вертикальных символов, заключение в них текста
def vLine(text):
    return ('| {} |').format(text)


# Ввод значений и создание переменных
text = str(input('Введите текст: '))
textLen = len(text)
horLine = hLine(textLen)
verLine = vLine(text)

# Вывод результатов
print(horLine)
print(verLine)
print(horLine)
