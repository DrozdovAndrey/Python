# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

def difference_max_min(list_of_numbers):
    i = 0
    while i < len(list_of_numbers):
        list_of_numbers[i] = round(list_of_numbers[i] - (int(list_of_numbers[i])),10)
        i += 1
    difference_number = round((max(list_of_numbers) - min(list_of_numbers)), 10)
    print(difference_number)


list_of_numbers = [1.1, 1.2, 3.1, 5.17, 10.02]
difference_max_min(list_of_numbers)
