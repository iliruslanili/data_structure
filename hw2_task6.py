# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.


import random

num = random.randint(0, 100)

for i in range(1, 11):
    user_num = int(input('Введите ваше число: '))
    if user_num == num:
        print(f'Вы угадали за {i} попыток!')
        break
    else:
        print('Ваше больше' if user_num > num else 'Ваше меньше')
print(f'Загаданное число: {num}')