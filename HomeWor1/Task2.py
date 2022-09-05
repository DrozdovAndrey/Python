# 2-Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

# def logical_statement(x, y, z):
#     print(f"{x}  {y}  {z}  {x}  {y}  {z}  {(not (x or y or z)) == (not x and not y and not z)}")
#     return (not (x or y or z)) == (not x and not y and not z)
# print('X  Y  Z ¬X ¬Y ¬Z')
# if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
# logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
# logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
#     print("Истинно")
# else:
#     print("Ложно")

# решение 2
def check():
    print("-"*15)
    print('X','Y','Z', 'result', sep='  ')
    print("-"*15)
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                result = not(X or Y or Z) == (not(X) and not(Y) and not(Z))
                print(f'{X}  {Y}  {Z} - {result}')

check()

