# # print('hello world')

# # переменные
# # int, float, boolean, str, list, None
# # value = None
# # print(type(value))
# a = 123
# b = 1.23
# # print(type(a))
# # print(type(b))
# # value = 1234
# # print(type(value))

# s = 'hello world'
# # print(type(s)) # вывод данных

# # s = 'hello "world'
# # print(s)

# # s = "hello 'world"
# # print(s)

# # s = 'hello \' world' # обратный слеш может вывести '
# # print(s)

# # s = 'hello \n world' # обратный слеш n  выводит на нровую строку
# # print(s)

# # print(a, b, s)

# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = True
# print(f)

# list = ['1', '2', '3', 'hello']
# print(list)

# list = ['1', '2', '3', 'hello', 1, 2, 3, True]
# #  print(list) # пробел может все сломать, этот код не запустится
# print(list)


# ввод данных input
# print('Введите a')
# # a = input()
# a = int(input()) # усли мы хотим получить число а не строку нужно указать что мы хотим
# print('Введите b')
# # b = input()
# b = int(input())
# # print(a, b)
# # print('{} {}'.format(a, b))
# # print(f'{a} {b}')
# print(a, '+', b, ' = ', a + b)


# арифметические операции

# a = 1.3
# b = 3
# # округляет до целого, или до любого знака после запчятой в примере до 5
# c = round(a*b, 5)
# print(c)

# a = 3
# # a = a+5
# a += 5
# print(a)


# логические операции

# a = 1 > 3 and 5>2
# a = 'qwe'
# b = 'qwe'
# a = [1, 2]
# b = [1, 2]
# a = 1<3<5
# func = 1
# T = 4
# x = 123


# print(func<T>(x))


# f = 1>2 or 4 <6
# print(f)

# f=[1,2,3,4]
# # print(2 in f)

# # is_odd = f[0]%2==0
# is_odd = not f[0]%2
# print(is_odd)

# a = int(input('a='))
# b = int(input('b=1'))
# if a>b:
#     print(a)
# else:
#     print(b)

# user_name = input('Введите имя: ')
# if user_name == 'Андрей':
#     print('Privet Andrey')
# elif user_name == 'Igor':
#     print('Privet gamer')
# else:
#     print('Privet, Dude')

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original%10)
#     original//=10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original%10)
#     original//=10
# else:
#     print('Pogalui')
#     print('hvatit')
# print(inverted)
# for i in 1,2,3,4,5:
# list = [1,2,3,5,10,2]
# for i in list:
#     print(i)

# r= range(10)
# for i in r:
#     print(i)

# for i in range(5):
#     print(i)
# for i in range(1,10,2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# ran = range(1,6)
# numbers = list(ran)
# print(numbers)
# numbers[0]=10
# print(numbers)
# print(f'{len(numbers)} len')
# for i in numbers:
#     i*=2
#     print(i)
# print(numbers)

def f(x):
    if x == 1:
        return 'Целое'
    elif x==2.3:
        return 23
    else:
        return
arg = 1
print(f(arg))
print(type(f(arg)))