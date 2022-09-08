# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial():
    while True:
        input_num = input('Введите чило больше 0: ')
        try:
            input_num = int(input_num)
            list_factorial = list(range(1,input_num+1))
            
            factorial = 1
            for i in list_factorial:
                factorial *= i
                list_factorial[i-1] = factorial
                
            print(list_factorial)
            break
        except ValueError:
            print('Вы ввели неправильные данные!')    


factorial()