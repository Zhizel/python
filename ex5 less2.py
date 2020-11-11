start_list = [9,8,7,6,6,5,4,4,1]
print('Cтартовый рейтинг', start_list)
user_num = int(input('Введите число от 1 до 9: '))
a = 0
for x in start_list:
    if user_num <= x:
        a += 1
start_list.insert (a, user_num)
print('Обновленный рейтинг', start_list)
