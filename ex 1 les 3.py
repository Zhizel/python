a1=int(input("Введите делимое : "))
a2=int(input("Введите делитель : "))
def division(a1, a2):
    try:
        return a1/a2
    except ZeroDivisionError as err:
        print( 'Ошибка! Деление на ноль недопустимо')

print('Результат деления: ', division(a1, a2))