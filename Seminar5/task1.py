import random


def random_koef(n):
    koef_list = []
    for i in range(0, n):
        koef_list.append(random.randint(0, 100))
        if i == 0:
            while koef_list[0] == 0:
                del koef_list[0]
                koef_list.append(random.randint(0, 100))
    # return koef_list
    print(koef_list)


# def gen


def number_input(input_string):
    '''
    Функция для проверки ввода числа.
    '''
    while type:
        digit = input(input_string)
        try:
            digit = int(digit)
            return digit
        except ValueError:
            print("Введено неверное значение. Только числа!!!")


n = number_input('введите степень полинома: ')
random_koef(n)
