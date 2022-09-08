# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

import time


def get_random(a,b):
    while True:
        if a >= 0 and b <= 9:
            time_ns = round(time.perf_counter_ns()/100)%10
            if time_ns > a and time_ns < b:
                print(time_ns)
                break
        elif a>=0 and b <= 99:
            time_ns = round(time.perf_counter_ns()/100)%100
            if time_ns > a and time_ns < b:
                print(time_ns)
                break
        elif a>=0 and b <= 999:
            time_ns = round(time.perf_counter_ns()/100)%1000
            if time_ns > a and time_ns < b:
                print(time_ns)
                break
        elif a>=0 and b <= 9999:
            time_ns = round(time.perf_counter_ns()/100)%10000
            if time_ns > a and time_ns < b:
                print(time_ns)
                break
        

def get_number():
    while True:
        a = input('Введите границы диапазона (): ')
        
        try:
            a = int(a)
            
            return a
            
            
        except ValueError:
            print('Вы ввели неправильное значение')

get_random(get_number(), get_number())

