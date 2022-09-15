# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

from pydoc import text


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


with open('coding.txt','w', encoding= 'utf_8')  as data:
    data.write(input())
with open('coding.txt','r', encoding= 'utf_8')  as data:
    text = data.readline()


print(f"Текст после кодировки: {coding(text)}")
with open('decoding.txt','w', encoding= 'utf_8')  as data:
    data.write(coding(text))

print(f"Текст после дешифровки: {decoding(coding(text))}")