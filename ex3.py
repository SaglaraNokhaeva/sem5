# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили. Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.

# 1 способ
my_str = input('Введите строку: ')
my_dictcomp = {my_str[i]: ord(my_str[i]) for i in range(len(my_str))}
print(my_dictcomp)
dict_iter = iter(my_dictcomp.items())
for i in range(5):
    print(*next(dict_iter))


