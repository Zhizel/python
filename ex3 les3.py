def max_sum (*args):
    return sum(args) - min(args)

first = int(input('Введите первый аргумент: '))
second = int(input('Введите второй аргумент: '))
third = int(input('Введите третий аргумент: '))

print('Сумма наибольших двух: ', max_sum(first, second, third))
