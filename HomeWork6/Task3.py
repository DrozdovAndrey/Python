# 3 - Найти расстояние между двумя точками пространства(числа вводятся через пробел)

def point_distance():
    while True: 
        print('Введите координаты двух точек (A и B, через пробел: a1 a2 b1 b2)')
        
        try:
            input_list = list(map(int, input().split()))
            print(input_list)
            check_range_points = lambda a1, a2, b1, b2: (round((int((b1 - a1))**2+int((b2 - a2))**2)**0.5, 2))
            print(check_range_points(input_list[0], input_list[1], input_list[2], input_list[3]))
            
            break
        except ValueError:
             print('Вы ввели непонятные символы')

point_distance()

