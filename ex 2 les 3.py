name=input('Введите ваше имя: ')
surname=input('Введите вашу фамилию: ')
b_day = input('Дату рождения: ')
city = input('Введите город проживания: ')
e_mail = input('Введите e-mail: ')
phone = input('Введите номер телефона: ')
def user (name, surname, b_day, city, e_mail, phone):
    return f'Имя: {name}', f"Фамилия: {surname}", f'День рождения: {b_day}', f'Город проживания: {city}', f'Электронная почта: {e_mail}', f'Телефон: {phone}'
print ('Данные о пользователе одной строкой:', user (name, surname, b_day, city, e_mail, phone))