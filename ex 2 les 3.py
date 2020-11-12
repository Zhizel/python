def user (name, surname, b_day, city, e_mail, phone):
    Rezult='Имя: ' + f'{name}' + ' Фамилия: ' + f'{surname}' + ' День рождения: ' + f'{b_day}' + ' Город проживания: ' + f'{city}' + ' Электронная почта: ' + f'{e_mail}' + ' Телефон: ' + f'{phone}'
    return Rezult



name=input('Введите ваше имя: ')
surname=input('Введите вашу фамилию: ')
b_day = input('Дату рождения: ')
city = input('Введите город проживания: ')
e_mail = input('Введите e-mail: ')
phone = input('Введите номер телефона: ')


print ('Данные о пользователе одной строкой:', user (name, surname, b_day, city, e_mail, phone))