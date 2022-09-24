# 1 - Определить, присутствует ли в заданном списке строк, некоторое число

find_number = 9
input_list = [l for x in ['hsfhvkh69', 'srifgkrgfk', '6', 'hkjdrhkfhd', 'hfkjehf6', '6'] for l in x if l == str(find_number)]
result = lambda input_list: 'Такой элемент есть в списке' if input_list else 'Такого элемента нет'

print(result(input_list))
