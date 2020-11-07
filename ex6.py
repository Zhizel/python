day = 1
start = float(input( 'Введите результат первого дня (в км.): '))
finish = int(input('Введите количество км, которое нужно будет пробегать :  '))
while finish > start:
    start += start * 0.1
    day += 1
print(f'Спортсмен достигнет результата через {day} дней')