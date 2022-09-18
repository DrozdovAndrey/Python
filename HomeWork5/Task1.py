# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

def remove_word(input_text, find_part):
    res = [i for i in input_text if not find_part in i]
    return res
    
def text_sum(res):
    out = ''
    for i in res:
        out += i + ' '
    return out

def split_text(input_text):
    input_text = input_text.split()
    return input_text

input_text = 'абвгдейка - это передача'
print(input_text)
input_text = split_text(input_text)
find_part = 'абв'
# print(input_text)
res = remove_word(input_text, find_part)
out = text_sum(res)
# print(res)
print(out)


