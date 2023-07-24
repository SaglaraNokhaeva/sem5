# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.


# 1 способ
# str = input('Введите строку: ')
# my_dictcomp = {str[i]: ord(str[i]) for i in range(len(str))}
# print(my_dictcomp)

# 2 способ
from pprint import pprint
pprint(my_dictcomp := {i: ord(i) for i in input('Введите строку: ')}, width=1)
