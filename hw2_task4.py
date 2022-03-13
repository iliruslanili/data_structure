# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

def my_range(num):
    buff = -2
    for i in range(num):
        buff /= -2
        yield buff


summ = 0
for i in my_range(int(input('Введите число элементов: '))):
    summ += i
print(summ)
