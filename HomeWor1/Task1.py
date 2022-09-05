# 1-Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

def check_weekend():
    while True:
        weekdays = ['Понедельник', 'Вторник', 'Среда',
                    'Четверг', 'Пятница', 'Суббота', 'Воскресение']
        print('Введите число обозначающее день недели \n(Понедельник -1, Вторник - 2, Среда - 3, Четверг - 4,\n Пятница - 5, Суббота - 6, Воскресение - 7')
        input_number1 = input()
        try:
            input_number = int(input_number1)
            if input_number > 0 and input_number < 8:
                if input_number == 6 or input_number == 7:
                    print(f'Сегодня {weekdays[input_number-1]} и это выходной')
                    break
                else:
                    print(f'Сегодня {weekdays[input_number-1]} и нужно работать')
                    break
            else:
                print('Вы ввели неправиьные число')
        except ValueError:
             print('Вы ввели непонятные символы')

check_weekend()