# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


print(*(i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8))
# map(int, str(i)) даёт нам список цифр числа, например: [1, 2]
