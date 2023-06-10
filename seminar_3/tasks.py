# дан сптсок чисел, определить сколько в нем различных чисел.

# list=[1,1,2,0,-1,3,4,4]
# print(list)
# set - множества выводит уникальные значения.
# import random
# number=int(input("Введите максимум чисел: "))
# num=[]
# for i in range (number):
#     num.append(random.randint(-3,3))
# print(num)
# print(len(set(num)))


# print(len(set(input().split())))


# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# lst=list(map(int,input("Введите значения: ").split()))
# k = int(input("Введите k: "))
# for i in range(k):
#     lst.insert(0, lst.pop())
# print(*lst)



# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# strip - убирает лишние пробелы и  тд

# dictionary = {}
# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# list = set()
# for i in dictionary:
#     for j in i.keys():
#         list.add(i[j].strip()) 
# print(list)

# print(set([list(i.values())[0].strip() for i in dictionary]))


# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# import random
# number=int(input("Введите максимум чисел: "))
# num=[]
# for i in range (number):
#     num.append(random.randint(-3,3))
# print(num)
# count=0
# for i in range(number-1):
#     if num[i+1]>num[i]:
#         count+=1
# print(count)




                 













