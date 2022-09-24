# 4 - Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

input_string = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
find_string = 'qwe'
try:
    second_input = [x for x in range(len(input_string))[input_string.index(find_string)+1::] if input_string[x] == find_string]
    if second_input:
        print (f'Второе вхождение элемента под индексом: {second_input[0]}')
    else:
        print('Второго вхождения нет')
except ValueError:
    print('Такого элемента нет в списке')