# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# 3. Удалите в целочисленном массиве все положительные числа, которые являются палиндромами.
# Дополнения и пояснения:
# 1. В списке строк ['fdg5', 'dfgrd7', '8', fdgdf', 'trr'] пользователь ищет 5. Нужно написать, что число есть в списке. Можете даже подумать, как вывести индекс элемента.
# 2. 
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# 3. Используйте свою функцию из другого модуля

# 4. Дополнительное задание. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# 5. Дополнительное задание. Проверьте, является ли данный массив (аргумент в функции) возрастающим или убывающим.


# будет время надо сделать задачки

def find_num(st):
    if st.find('5') > 0:
        print('Число присутствует')




list_input = ['fdg5', 'dfgrd7', '8', 'fdgdf', 'trr']