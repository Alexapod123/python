# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

n = int(input('Введите количество элементов: ')) #общее кол-во эл-в
x = int(input('Введите первый элемент: '))
d = int(input('Введите шаг прогрессии: ')) #шаг
print(*range(x, x + d * n, d))