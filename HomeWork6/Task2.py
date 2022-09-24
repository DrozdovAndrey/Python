# 2 - Найти сумму чисел списка стоящих на нечетной позиции

list_numbers = [4,5,1,10,3]
odd_index = [list_numbers[i] for i in range(len(list_numbers)) if i%2]
print(sum(odd_index))