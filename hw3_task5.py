# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

samples = [random.randint(-10, 10) for _ in range(10)]
max_negative = -10  # минимальное значение диапазона чисел
print(samples)
no_negative = True  # для проверки отсутствия отрицательных чисел
# Очистим массив от неотрицательных чисел

for i, item in enumerate(samples[:]):
    if item >= 0:
        samples.remove(item)
    else:
        max_negative = item if max_negative < item else max_negative
        no_negative = False

print(samples)  # После очистки
print(f'Максимальное отрицательное: {max_negative}' if not no_negative else 'Отрицательные числа отсутствуют')
