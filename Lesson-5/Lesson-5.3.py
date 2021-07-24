# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('Salary.txt', 'w+') as sal_file:
    sal_file.writelines(['Smith 18000\n', 'Cooper 50000\n', 'Bloom 15000\n', 'Fowler 41000\n'])
    sal_file.seek(0)
    sal_file_lines = sal_file.readlines()
    surname_list = []
    salary_list = []
    for el in sal_file_lines:
        surname, salary = el.split()
        surname_list.append(surname)
        salary_list.append(int(salary))
    average_salary = sum(salary_list) / len(salary_list)
    print(f'Средняя величина дохода сотрудников - {average_salary}')
    salary_list_less = []
    for val in salary_list:
        if val < 20000:
            salary_list_less.append(surname_list[salary_list.index(val)])
    print(f'Зарплата менее 20 тысяч у сотрудников {", ".join(salary_list_less)}')

