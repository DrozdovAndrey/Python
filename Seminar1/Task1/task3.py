# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
#     *Примеры:* 
    
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5


number = int(input('введите число n = '))
minus_number = number*(-1)
while number >= minus_number:
    print(minus_number)
    minus_number +=1
    