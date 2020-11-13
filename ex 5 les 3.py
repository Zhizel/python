def summary():
   result_sum = 0
   while True:
       num_list = input('Введите числа через пробелы или $ для заврешения: ').split()
       if num_list.count('$'):
           result_sum += sum(map(int, num_list[:num_list.index('$')]))
           break
       result_sum += sum(map(int, num_list))
       print(f'Сумма до конца строки {result_sum}')
   return result_sum


print('Cумма до спец символа $: ', summary())