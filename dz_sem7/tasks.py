# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 

# dict = 'аоуэыяеёюи'
# poem = input('Введите стихотворение: ').split()
# result = [sum([True for j in word if j.lower() in dict]) for word in poem]

# print(result)

# if all(result) and len(set(result)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")


# Напишите функцию
# print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns
# указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет
# с единицы (подумайте, почему не с нуля).

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows+1 ):
        for j in range(1, num_columns +1):
            print(f"{operation(i, j):4}", end=" ")
        print()

print_operation_table(lambda x, y: x * y)

 