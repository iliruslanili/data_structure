# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

samples = [i for i in range(2, 100)]
multiplicity = {i: 0 for i in range(2, 10)}

for val in samples:
    for key in multiplicity.keys():
        multiplicity[key] += 1 if val % key else 0

print(multiplicity)
