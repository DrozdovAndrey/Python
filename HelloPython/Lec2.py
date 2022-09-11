# colors = ['red', 'green','blue123']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('Line 12\n')
# data.write('Line 13\n')
# data.close()

# после окончания блока произойдет разрыв с файлом
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')


# exit() # функция не дает запускать код после себя
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# import lec as l

# print(l.f(1))

# def new_string(symbol, count):
#     return symbol*count

# print(new_string('!', 5))
# print(new_string('!'))  - здесь будет ошибка, не указан count

# def new_string(symbol, count = 3):
#     return symbol*count

# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(5))


# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a','s','d','w'))
# print(concatenatio('a', '1'))
# print(concatenatio(1,2,3,4))  - ломается логика, нужны строки, а не числа

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1,10):
#     list.append(fib(e))
# print(list)

# a = (3,4,5)
# print(a)
# print(a[0])
# print(a[-2])
# a[0] = 12 - не сработает
# t = ()
# print(type(t))

# t= (1,)
# print(type(t))

# t = 1
# print(type(t))

# t = (28, 10, 1234)
# print(type(t))

# colors = ['red','green','blue','yelow']
# print(colors)

# t = tuple(colors)
# print(t)

# a = (3,4,5)
# for i in a:
#     print(i)


# colors = ['red','green','blue','yelow']


# t = tuple(colors)
# red, green, blue, yelow = t  # распаковываем кортеж в независимые переменные
# print('r: {} g: {} b: {} y: {}'.format(red, green, blue, yelow))

# dictionary = {}
# # \ используется чтобы писать с новой строки 
# dictionary = \
#     {
#         'up': '⬆',
#         'down': '⬇',
#         'left': '⬅',
#         'right': '➡'
#     }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.keys():
#     print(k)

# for k in dictionary.values():
#     print(k)

# for k in dictionary:
#     print(k)

# print(dictionary['up'])
# dictionary['up'] = 'up'
# print(dictionary['up'])

# colors = {'red','green','blue'}
# print(colors)
# colors.add('red')
# print(colors)
# colors.add('grey')
# print(colors)
# colors.remove('red')
# print(colors)
# # colors.remove('red') - если нет такого значения в множетсве вызовет ошибку
# colors.discard('red')  # - это не вызовет
# print(colors)
# colors.clear
# print(colors)

# a = {1,2,3,5,8}
# b = {2,5,8,13,21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i = a.intersection(b)
# print(i)
# dl = a.difference(b)
# print(dl)
# dr = b.difference(a)
# print(dr)
# # {1, 2, 3, 5, 8}
# # {1, 2, 3, 5, 8, 13, 21}
# # {8, 2, 5}
# # {1, 3}
# # {13, 21}

# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# print(q)
# # {1, 21, 3, 13}

# s = frozenset(a)

# если заморозить множество то никакие функции работать не будут

