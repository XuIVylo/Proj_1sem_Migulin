# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 3 – 8.
# Задача взята из ПЗ 7-1
# Дана строка. Подсчитать количество содержащихся в ней латинских букв.

import tkinter as tk


def letters():
    s = str(s1.get())
    a = 0
    for i in s:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            a += 1
    res.config(text='Количество латинских букв в строке: {}'.format(a))


root = tk.Tk()
root.geometry('300x100')
root.configure(bg='#00466C')
root.title('PZ_12_2')
res = tk.Label(root, text='Введите произвольную строку:', bg='#00466C', fg='white')
res.pack()
s1 = tk.Entry(root, bg='#002F48', fg='white')
s1.pack()
button = tk.Button(root, text='Подсчитать кол-во букв', command=letters, bg='#0079BA', fg='white')
button.pack()
res = tk.Label(root, text='Результат:', bg='#00466C', fg='white')
res.pack()

root.mainloop()