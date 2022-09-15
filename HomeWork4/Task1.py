# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def check_input_int():
    while True:
        try:
            input_num = int(input('Введите натуральное число: '))
            if input_num > 0:
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')

def compiler_prime_factors(input_num):
    i = 2
    list_prime_numbers = []
    while i * i <= input_num:
        while input_num % i == 0:
           list_prime_numbers.append(i)
           input_num = input_num // i
        i = i + 1
    if input_num > 1:
       list_prime_numbers.append(input_num)
    print(list_prime_numbers)


input_num = check_input_int()
compiler_prime_factors(input_num)

   
