# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def sum_pair(input_list):
    i=0
    sum_list = []
    while i < len(input_list)/2:
        sum_list.append((input_list[i]*input_list[-i-1]))
        i+=1
    print(sum_list)

input_list = [2,3,5,6]
sum_pair(input_list)