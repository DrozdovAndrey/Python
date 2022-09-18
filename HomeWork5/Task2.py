# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
import random


def check_input_int():
    while True:
        try:
            input_num = int(input('Ввеите число от 1 до 28: '))
            if input_num > 0 and input_num < 29:
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')

def get_toss():
    toss = True
    r = random.randint(0,1)
    if r == 0:
        toss = False
    return toss

def get_candy():
    while True:
        try:
            input_num = int(input('Ввеите число конфет. Для интереса не вводите значение меньше 100: '))
            if input_num > 99:
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')
def the_game(flag, all, player1_name, player2_name):
    while all > 0:
        if flag:
            print(f'Ход игрока {player1_name}')
            player1 = check_input_int()
            all -= player1
            print(all)
            flag = False
            if all == 1:
                print(f'Игрок {player1_name} выиграл')
                break
        else:
            print(f'Ход игрока {player2_name}')
            player2 = check_input_int()
            all -= player2
            print(all)
            flag = True
            if all == 1:
                print(f'Игрок {player2_name} выиграл')
                break

def get_name():
    name = input('Введите ваше имя:')
    return name

all = get_candy()
print(f'Всего {all}')
flag = get_toss()
player1_name = get_name()
player2_name = get_name()
the_game(flag, all, player1_name, player2_name)
