# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

my_gen = (i for i in range(0, 101, 2) if i%2==0 )
for char in my_gen:
    print(char)