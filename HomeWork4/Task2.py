# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]





def check_input_list():
    while True:
        input_list = input('Введите числа через пробел: ')
        try:
       
            input_list = input_list.split(' ')
            for i in input_list:
                i = int(i)
            return input_list
        
        except ValueError:
            print('Вы ввели неправильные данные!')    

def show_not_repit_element(input_list):
    new_lst = []
    [new_lst.append(i) for i in input_list if i not in new_lst]
    print(new_lst)


input_list = check_input_list()
print(input_list)
show_not_repit_element(input_list)

