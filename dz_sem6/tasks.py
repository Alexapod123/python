# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# n = int(input('Введите количество элементов: ')) #общее кол-во эл-в
# x = int(input('Введите первый элемент: '))
# d = int(input('Введите шаг прогрессии: ')) #шаг
# print(*range(x, x + d * n, d))


# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = int(input())
max_number = int(input())
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)