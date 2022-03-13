# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

min_index, max_index = 0, 0
samples = [random.randint(-100, 100) for _ in range(10)]

for i, val in enumerate(samples):
    min_index = i if samples[i] < samples[min_index] else min_index
    max_index = i if samples[i] > samples[max_index] else max_index

print(samples)
print(f'min: {samples[min_index]}\t max: {samples[max_index]}')
samples[min_index], samples[max_index] = samples[max_index], samples[min_index]
print(samples)
