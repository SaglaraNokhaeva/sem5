# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел, начиная с числа 2.
# ✔ Для проверки числа на простоту используйте правило: «число является простым, если делится
# нацело только на единицу и на себя».



def generator(n):
    count = 0
    current = 2
    while count < n:
        flag = True
        for i in range(2, current):
            if not current % i:
                flag = False
        current += 1
        if flag:
            count += 1
            yield current - 1


generate = generator(int(input("Введите целое положительное число: ")))
print(*generate)
