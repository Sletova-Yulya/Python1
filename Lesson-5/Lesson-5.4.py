# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

with open('Numbers.txt', 'r') as num_file:
    a = num_file.readlines()
    print(a)
    str1, str2, str3, str4 = a[0], a[1], a[2], a[3]
    new_str1 = str1.replace('One', 'Один')
    new_str2 = str2.replace('Two', 'Два')
    new_str3 = str3.replace('Three', 'Три')
    new_str4 = str4.replace('Four', 'Четыре')
    with open('New_numbers.txt', 'w', encoding='utf-8') as new_num_file:
        print(new_str1, file=new_num_file)
        print(new_str2, file=new_num_file)
        print(new_str3, file=new_num_file)
        print(new_str4, file=new_num_file)


