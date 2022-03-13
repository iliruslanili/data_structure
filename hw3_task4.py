# 4. Определить, какое число в массиве встречается чаще всего.
import random

samples = [random.randint(0, 5) for _ in range(20)]
unique = set(samples)
stats = {key: 0 for key in unique}
print(samples)

for value in samples:
    if stats.get(value, None) is not None:
        stats[value] += 1

maximum = 0
print(stats)
for key, val in stats.items():
    maximum = key if val > maximum else maximum

print(f'Чаще всего встречается число {maximum}. Оно встречается {stats[maximum]} раз')
