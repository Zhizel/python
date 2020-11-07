user_num = int (input('Введите целое число больше 0:'))
max_num = 0
num=user_num
while num>0:
    last_num=num % 10
    if last_num > max_num:
        max_num=last_num
    num=num // 10
print('Самая большая цифра в числе', user_num,'это',max_num)


