# 2-Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. 
# Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

def logical_statement(x, y, z):
    print(f"{x}  {y}  {z}  {x}  {y}  {z}  {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)
print('X  Y  Z ¬X ¬Y ¬Z')
if (logical_statement(0, 0, 0) and logical_statement(0, 0, 1) and logical_statement(0, 1, 0) and 
logical_statement(0, 1, 1) and logical_statement(1, 0, 0) and logical_statement(1, 0, 1) and
logical_statement(1, 1, 0) and logical_statement(1, 1, 1)):
    print("Истинно")
else:
    print("Ложно")
