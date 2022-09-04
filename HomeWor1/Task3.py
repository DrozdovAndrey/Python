# 3- Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

def quater_number():
    while True:
        input_x = input('Введите координаты по оси х (не равное 0): ')
        input_y = input('Введите координаты по оси y (не равное 0): ')
        try:
            input_x = float(input_x)
            input_y = float(input_y)
            if input_x != 0 and input_y != 0:
                if input_x > 0 and input_y > 0:
                    print('Точка в первой четверти')
                    break
                elif input_x > 0 and input_y < 0:
                    print('Точка во второй четверти')
                    break
                elif input_x < 0 and input_y < 0:
                    print('Точка в третьей четверти')
                    break
                else:
                    print('Точка в четвертой четверти')
                    break
            else:
                print('Вы ввели неправиьные число')
        except:
             print('Вы ввели непонятные символы')

quater_number()