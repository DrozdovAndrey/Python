# 2. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел. НОК - наименьшее общее кратное, которое делится и на первое, и на второе число. 


input_1 = int(input())
input_2 = int(input())

if input_1 > input_2:
    input_1, input_2 = input_2, input_1
for i in range(1, input_2 +1):
    if (input_1*i)%input_2 == 0:
        print((input_1*i))
        break