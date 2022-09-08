# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11



def sum_float():
    while True:
        input_num = (input('Введите вещественное число(Например:56.765): '))
        try:
            input_num = abs(float(input_num))
            input_num = str(input_num)
            input_list = list(input_num)
            input_list.remove('.')
            
            print(input_list)
            sum_num = 0
            for i in input_list:
                i = int(i)
                sum_num = sum_num + i
            print(sum_num)
            break
            
            
        except ValueError:
             print('Вы ввели непонятные символы')

sum_float()