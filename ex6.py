# ✔ Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт» без перехода на новую строку.

# print(*('FizzBuzz' if not i % 15 else 'Buzz' if not i % 5 else 'Fizz' if not i % 3 else i for i in range(1, 101)))

# решение из 1 семинара
# for i in range(2, 11):
#     for j in range(2, 6):
#         print(f"{j} * {i} = {i * j}", end='\t\t')
#     print()
# print()
# for i in range(2, 11):
#     for j in range(6, 10):
#         print(f"{j}*{i} = {i * j}", end='\t\t')
#     print()

# print(*(f"{j} * {i} = {i * j}\n" for i in range(2, 11) for j in range(2, 11)))

print(*('\t'.join(f"{i} * {j} = {i * j}\t\t" if i % 5 else f"{i} * {j} = {i * j}\n" for i in range(2, 6)) for j in range(2, 11)), sep='\n')
print(*('\t'.join(f"{i} * {j} = {i * j}\t\t"  for i in range(6, 10)) for j in range(2, 11)), sep='\n')