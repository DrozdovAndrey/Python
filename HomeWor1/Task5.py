# 5-Напишите программу, которая принимает на вход координаты
#  двух точек и находит расстояние между ними в 2D пространстве.

def point_distance():
    while True:
        print('Введите координаты двух точек (A: x1, y1; B: x2, y2)')
        input_x1 = input('Точка А, x1:')
        input_y1 = input('Точка А, y1:')

        input_x2 = input('Точка B, x2:')
        input_y2 = input('Точка B, y2:')
        try:
            input_x1 = float(input_x1)
            input_y1 = float(input_y1)
            input_x2 = float(input_x2)
            input_y2 = float(input_y2)
            print(((input_x2-input_x1)**2 + (input_y2-input_y2)**2)**0.5)
            break
        except ValueError:
             print('Вы ввели непонятные символы')

point_distance()