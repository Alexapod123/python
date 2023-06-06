#  на вход число, на выход факториал

# n = input ("Введите число: ")
# n = int(n)
# count = int(1)
# f = int(1)
# while count <= n:
#     f=count*f
#     count+=1
# print (f)





# вход число, выход каким число по счету в ряду фибоначчи,если нет, то выход -1

# n = int(input('Введите число: '))
# a = 0
# b = 1
# count = 2
# while b <= n:
#     if b == n:
#         print(count)
#         break
#     a,b = b, a+b
#     count+=1
# else:
#     print(-1)


# вход количество дней и темпартура в день, выход самая длинная оттпепель сколько дней

# n = int(input('Введите количество дней: '))
# count = 0
# max_count = 0

# for n in range (1, n+1):
#     tem = int(input("Введите температуру: "))
#     if tem > 0:
#         count+=1
#     elif tem<=0:
#         count=0
#     if count>max_count:
#         max_count=count
# print(max_count)




# вход количество арбузов, вторая строка массы арбузов. найти макс и мин



# n = int(input('Введите количество арбузов: '))
# mmax=0
# mmin=999
# for i in range(n):
#     m = int(input("Введите массу арбуза: "))
#     if m>mmax:
#         mmax=m
#     if m<mmin:
#         mmin=m
# print(mmax, mmin)
