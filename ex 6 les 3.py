def int_func(text):
    return text.capitalize()

text = input('Введите текст латиницей маленькими буквами: ')
print(''.join(map(int_func, text.split())))