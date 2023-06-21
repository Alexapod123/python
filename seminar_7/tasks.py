# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# values = [1, 23, 42, 'asdfg']
# trasformation = lambda i: i   
# transformed_values = list(map(trasformation, values))
# print(f'or: {values}')
# print(f'copy: {transformed_values}')
# if values == transformed_values:
#  print('ok')
# else:
#  print('fail')

# 


# def find_farthest_orbit(array):
#     max_sq = [(i[0]*i[1], i) for i in array if i[0] != i[1]]
#     return max(max_sq)[1]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# def same_by(condition, nums):
#     return len(set(map(condition, nums))) == 1

# values = [0, 2, 10, 6] 

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')