# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна 
# сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

t = input('Введите номер билета: ')
a = int(t[0]) + int(t[1]) + int(t[2])
b = int(t[3]) + int(t[4]) + int(t[5])
if a == b:
    print('Yes, HAPPY TICKET')
else:
    print('Nooo:(')