a = int(input('Введите первый аргумент: '))
b = int(input('Введите второй аргумент: '))
c = int(input('Введите третий аргумент: '))
def max_sum (*args):
    return sum(args) - min(args)

print('Сумма наибольших двух: ', max_sum(a, b, c))
