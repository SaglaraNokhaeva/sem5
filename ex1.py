# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

dct = {}
data = input('Введите числа через символ “/”: ').split('/')

# 1 способ
# dct[data[1]] = data[0]
# dct[data[2]] = data[3:]
# print(dct)

# 2 способ
dct = {data[1]: data[0], data[2]: data[3:]}
print(dct)
