user_list = list (input('Введите ряд чисел: '))
print(f'Ваш первичный список: {user_list}')
for a in range(1, len(user_list), 2):
    user_list[a - 1], user_list[a] = user_list[a], user_list[a-1]
print(f'Измененный список: {user_list}')