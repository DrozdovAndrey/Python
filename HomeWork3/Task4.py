# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def get_double(number10):    
    number2 = ''
    if number10 == 0:
        number2 = 0
    else:
        while number10 > 0:
            number2 = str(number10 % 2) + number2
            number10 = number10 //2
    print(number2)
number10 = int(input('Число в десятичной СС:'))
get_double(number10)