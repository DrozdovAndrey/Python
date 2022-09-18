# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.


def check_input_int():
    while True:
        try:
            input_num = int(input('Введите код(натуральное число): '))
            return input_num
        except ValueError:
            print('Вы ввели неправильное значение!')

def encrypt(text, key):
    crypt = ''
    for i,char in enumerate(text):
        crypt += chr(ord(char)+key)
    return(crypt)

def decrypt():
    with open('coding_cesar.txt','r', encoding= 'utf_8')  as data:
        encrypted_text = data.read()
    key = check_input_int()
    crypt_decrypted = ''
    for i,char in enumerate(encrypted_text):
        crypt_decrypted  += chr(ord(char)-key)
    return(crypt_decrypted)

def write_code(encrypted_text, key):
    with open('coding_cesar.txt','w', encoding= 'utf_8')  as data:
        data.write(f'{encrypted_text}\n')



text = input('Введите текст, который хотите зашифровать: ')
key = check_input_int()


encrypted_text = encrypt(text, key)
print(f'Зашиврованный текст: {encrypted_text}')
write_code(encrypted_text, key)
decrypted_text = decrypt()
print(f'Расшиврованный текст: {decrypted_text}')
