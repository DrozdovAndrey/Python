# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def cipher_encrypt(plain_text, key):
    encrypted = ""
    for c in plain_text:
        if c.isupper(): 
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 33 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): 
            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 33 + ord('a')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            encrypted += c
    return encrypted

def cipher_decrypt(ciphertext, key):
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('А')
            c_og_pos = (c_index - key) % 33 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - key) % 33 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            decrypted += c
    return decrypted

def check_input_int():
    while True:
        try:
            input_num = int(input('Введите натуральное число: '))
            return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')




n = check_input_int()
plain_text = "Ребята все по домам, губы синие!"
ciphertext = cipher_encrypt(plain_text, n)
with open('coding_cesar.txt','w', encoding= 'utf_8')  as data:
    data.write(ciphertext + str(n))

cipherdecrypttext = cipher_decrypt(ciphertext, n)
print("Оригинальный текст:\n", plain_text)
print("Зашифрованный текст:\n", ciphertext)
print("Расшифрованный текст:\n", cipherdecrypttext)
