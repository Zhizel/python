phr = input('Введите предложение: ')
words = phr.split()
a = 1
for w in words:
    print(f'{a}- е слово: {w[:10]}')
    a += 1