# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется.

languages = list(map(lambda language: language.upper(), ['python', 'c#', 'java', 'c++', 
                                                            'kotlin', 'swift', 'php', 
                                                            'java_script']))
numbers = [x for x in range(1, len(languages)+1)]                                                           
print(languages)
number_languages = list(zip(numbers, languages))
print(number_languages)

def swaped_number_languages(num_lan):
    filtered_list = []
    sum_ord = 0
    for num, lan in num_lan:
        for l in lan:
            sum_ord +=ord(l)
        if sum_ord % num == 0:
            filtered_list.append((sum_ord, lan))
    return filtered_list

print((swaped_number_languages(number_languages)))