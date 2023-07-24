# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.


# 1 способ
# str = input('Введите строку: ')
# my_dictcomp = {str[i]: ord(str[i]) for i in range(len(str))}
# print(my_dictcomp)

# 2 способ
from pprint import pprint
pprint(my_dictcomp := {i: ord(i) for i in input('Введите строку: ')}, width=1)
