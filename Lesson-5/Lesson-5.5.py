# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('New_file_3.txt', 'w+') as nf3:
    nf3.write('1 2 3 4 5 6')
    nf3.seek(0)
    nf3_data = nf3.read()
    num_list = nf3_data.split()
    num_sum = [int(elem) for elem in num_list]
    print(f'Сумма чисел равна {sum(num_sum)}')