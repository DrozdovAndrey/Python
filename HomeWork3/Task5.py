# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи](https://clck.ru/yWbkX.)



def fib1(n):
    if n == 0:
        return 0
    elif n in [1,2]:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)

list1 = []
for e in range(0,9):
    list1.append(fib1(e))

def fib2(n):
    if n == -1:
        return 1
    elif n == -2:
        return -1
    else:
        return fib2(n+2) - fib2(n+1)

list2 = []
for e in range(-8,0):
    list2.append(fib2(e))


list3 = list2 + list1
print(list3)

