# 3. Пользователь вводит время в минутах и расстояние в километрах. Найдите скорость в м/c..

# from time import time_ns


# time_minutes = float(input('Введите время в минутах: '))
# distance_km = float(input('Введите растояние в км: '))


# print((distance_km*1000)/(time_minutes*60))




# решения с функциями для всех 3х задач

def show_numbers(N):
    print([i for i in range(N*-1, N+1)])

def first_number_float(f1):
    if isinstance(f1, float):
        print(int((round(f1, 1)*10)%10))
    else:
        print('Нет')

def fins_speed():
    time_m = int(input('Введите время в минутах: '))
    distance_km = int(input('Введите растояние в км: '))
    print(f'Скорость = {round((distance_km*1000)/(time_m*60),2)} m/s')

show_numbers(5)
first_number_float(5.1)
fins_speed()