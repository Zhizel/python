def ex_1 ( c , b):
    return (c ** b)


def ex_2 ( c , b):
    n = b
    Rezultat=1
    while n<0:
        Rezultat = Rezultat/c
        n +=1
    return Rezultat



Osnova = float(input('Введите действительное положительное число: '))
Stepen = int(input('Введите целое отрицательное число: '))


print ('Результат возведения через **', ex_1( Osnova, Stepen))
print ('Результат возведения в степень через цикл', ex_2( Osnova, Stepen))






