# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def check_input_int(candy_per_move):
    while True:
        try:
            input_num = int(input(f'Ввеите число от 1 до {candy_per_move}: '))
            if input_num > 0 and input_num < candy_per_move + 1:
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
            input_num = int(input('Ввеите число конфет: '))
            if input_num > 99:
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')

def get_candy_per_move(candy_count):
    while True:
        try:
            input_num = int(input(f'Ввеите число конфет, которое будем брать за раз, но не больше чем {(candy_count//3)}: '))
            if input_num > 0 and input_num < (candy_count//3):
                return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')

def the_game(flag, candy_count, player1_name, player2_name):
    player1_move = 0
    count = 1
    while candy_count > 0:
        if flag:
            print(f'Ход игрока {player1_name}')
            player1_move = check_input_int(candy_per_move)
            candy_count -= player1_move
            print(f'Осталось {candy_count} конфет')
            flag = False
            count+=1
            if candy_count == 1:
                print(f'Игрок {player1_name} выиграл')
                break
        else:
            print(f'Ход игрока {player2_name}')
            player2_move = bot(candy_per_move, candy_count, player1_move, count)
            print(player2_move)
            candy_count -= player2_move
            print(f'Осталось {candy_count} конфет')
            flag = True
            count+=1
            if candy_count == 1:
                print(f'Игрок {player2_name} выиграл')
                break

def get_name():
    name = input('Введите ваше имя:')
    return name

def bot(candy_per_move, candy_count, player1_move, count):
    if count == 1:
        bot_move = (candy_count % (candy_per_move +1)) - 1
    else:
        bot_move = (candy_per_move +1) - player1_move
    return bot_move

   

candy_count = get_candy()
candy_per_move = get_candy_per_move(candy_count)
flag = get_toss()
player1_name = get_name()
player2_name = 'Бот Васька'
the_game(flag, candy_count, player1_name, player2_name)