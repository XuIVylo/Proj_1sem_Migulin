f1 = open('text18-14.txt', 'r', encoding='UTF-16')
a = f1.read()
print(a)
f1.close()

f1 = open('text18-14.txt', 'r', encoding='UTF-16')
c = len(a)
print('Количество символов:', c)
f1.close()

f2 = open('new_text18-14.txt', 'w', encoding='UTF-16')
b = a.upper()
f2.writelines(b)
f2.close()