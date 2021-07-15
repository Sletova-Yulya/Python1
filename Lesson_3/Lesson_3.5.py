# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

def sum_func():
    flag = 0
    total_sum = 0
    while flag == 0:
        num_str = input('Введите числа, разделяя пробелом, если хотите завершить работу программы, наберите @: ')
        list_1 = (num_str.split())
        list_2 = []
        try:
            for el in list_1:
                el = int(el)
                list_2.append(el)
        except ValueError:
            flag = 1
            print('Был введен спец. символ. Программа завершена.')
        total_sum = total_sum + sum(list_2)
        print(f'Сумма введенных чисел - {total_sum}')

z = sum_func()
print(z)
