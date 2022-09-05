# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

# 3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.

# 1
from itertools import count


def sequence(N):
    for i in range(N):
        print((-3)**i, end=' ')

# sequence(5)
#2
def sum_element(array_element):
    min_index = array_element.index(min(array_element))
    max_index = array_element.index(max(array_element))
    if min_index < max_index:
        res_array = array_element[min_index:max_index+1]
    else:
        res_array = array_element[max_index:min_index+1]
    print(res_array)
    print(sum(res_array))

# sum_element([1,2,5,4,7,9])
# sum_element([10,22,5,4,7,9])

#3

def count_elem(list_elem):
    max_elem = max(list_elem)
    max_elem_10 = max_elem - max_elem/10
    count_element = 0
    for i in list_elem:
        if i != max_elem:
            if i >= max_elem_10:
                count_element +=1
    print(count_element)

# count_elem([10,22,5,4,20,9,21])

#4 сортровка пузырьком

list_num = [10,8,7,10,5,9,4]
n = len(list_num)
for i in range(n-1):
    for j in range(n-i-1):
        if list_num[j] > list_num[j+1]:
            list_num[j], list_num[j+1] = list_num[j+1], list_num[j]
print(list_num) 