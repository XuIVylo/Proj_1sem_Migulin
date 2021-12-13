# Выполнить сортировку словаря d = {'a': 1, 'b': 2, 'c': 3} по убыванию
d = {'a': 1, 'b': 2, 'c': 3}
list_k = list(d.keys())
list_k.sort(reverse=True)
for i in list_k:
    print(i, ":", d[i])
