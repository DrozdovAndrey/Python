# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def sum_odd_index(list_of_numbers):
    sum_numbers = 0
    i=1
    while i < len(list_of_numbers):
        sum_numbers+=list_of_numbers[i]
        i+=2
    print(sum_numbers)

list_of_numbers = [2,3,5,9,3,7,9,-9,-9]
sum_odd_index(list_of_numbers)