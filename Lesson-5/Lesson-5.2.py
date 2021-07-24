# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('New_file_2.txt', 'w+') as new_f_2:
    new_f_2.writelines(['I like to read\n', 'I like to play\n', 'I like to study\n', 'Every day\n'])
    new_f_2.seek(0)
    new_list = new_f_2.readlines()
    len_new_f_2 = len(new_list)
    print(f'Количество строк в файле {len_new_f_2}')
    cycle_count = 1
    while cycle_count <= len_new_f_2:
        for strn in new_list:
            print(f'В строке {cycle_count} - {len(strn.split())} слов(a)')
            cycle_count += 1
