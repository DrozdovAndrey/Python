# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Пример:
# Волков Андрей 5
# Наталья Тарасова 5
# Фредди Меркури 3
# Денис Байцуров 4

# Программа выдаст:
# ВОЛКОВ АНДРЕЙ 5
# НАТАЛЬЯ ТАРАСОВА 5
# Фредди Меркури 3
# Денис Байцуров 4


# with open('FIO1.txt','a', encoding= 'utf_8')  as data:
#     data.write(f'{input()} \n')
#     data.write(f'{input()} \n')
#     data.write(f'{input()} \n')
#     data.write(f'{input()} \n')


def reading_data():
    with open('FIO1.txt', 'r', encoding= 'utf_8')  as data:
        new_data = data.readlines()
    return new_data
def rewrite_data(new_data):    
    with open('FIO1.txt', 'w', encoding= 'utf_8')  as data:   
        for line in new_data:
            if '5' in line:
                data.write(f'{line.upper()}')
            else:
                data.write(f'{line}')


new_data = reading_data()
rewrite_data(new_data)            

