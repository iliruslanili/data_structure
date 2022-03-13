import traceback


def read_input():
    a, b = input('Введите А: '), input('Введите B: ')
    operation = input('Введите операцию(+, -, *, /, 0-конец):')
    return a, b, operation


op = None

while op != '0':
    try:
        a, b, op = read_input()

        while op not in ['+', '-', '*', '/', '0']:
            op = input('Введите корректную операцию: ')

        if op == '/' and b == '0':
            raise ZeroDivisionError('На ноль делить нельзя!')

        if op == '0':
            break

        result = eval(f'{a}{op}{b}')
        print(result)
    except Exception as e:
        print('НЕКОРРЕКТНЫЕ ДАННЫЕ')
        print(e)
        traceback.print_exc()