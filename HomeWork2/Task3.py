# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа.

def polindrom():
    while True:
        input_num = input('Введите чило: ')
        try:
            
            input_num = int(input_num)
            polindrom_find(input_num)
            break
                   
                   

        except ValueError:
            print('Вы ввели неправильные данные!')    

def polindrom_find(input_num):
    input_num = str(input_num)
    input_list = list(input_num)
    # print(input_list)
    reverse_input_list = input_list
    reverse_input_list.reverse()
    # print(reverse_input_list)
    reverse_input_num = "".join(reverse_input_list)
    print(f'Перевернутое: {reverse_input_num}')
    if input_num == reverse_input_num:
        
        print('   Это полиндром')
    else:
        input_num = int(input_num) + int(reverse_input_num)
        print(f'Сумма  чисел: {input_num}')
        polindrom_find(input_num)

polindrom()

