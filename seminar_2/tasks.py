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

n = int(input('Введите число: '))
a = 0
b = 1
count = 2
while b <= n:
    if b == n:
        print(count)
        break
    a,b = b, a+b
    count+=1
else:
    print(-1)



