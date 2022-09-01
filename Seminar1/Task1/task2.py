# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# for i in range(5):
#     num = int(input())
#     if i == 0:
#         max = num
#     else:
#         if num > max:
#             max = num
# print()
# print(max)


# list_number = []
# for i in range(5):
#     list_number.append (int(input('Введите числа -'))) 
# max_number = list_number[0]
# for num in list_number:
#     if max_number < num:
#         max_number = num
# print(max_number)

# numbers = [int(i) for i in input().split(',')[:5]]
# max_number = numbers[0] 
# for j in numbers:
#     if j > max_number:
#         max_number = j
# print(max_number)

print(max([int(i) for i in input().split(',')[:5]]))


