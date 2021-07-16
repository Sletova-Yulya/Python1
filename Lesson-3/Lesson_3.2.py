# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def get_person (name, surname, birth_year, city, email, phone):
    """
    Функция формирует в одну строку информацию о пользователе.
    :param name: str, Имя
    :param surname: str, Фамилия
    :param birth_year: int, Год рождения
    :param city: str, Город проживания
    :param email: str, Адрес электронной почты
    :param phone: str, Номер телефона
    :return: str, Информация о пользователе
    """
    print(f'{name} {surname}, {birth_year} года рождения, проживает в городе {city}, адрес электронной почты {email}, телефон {phone}')

get_person('Юлия', 'Слетова', 1983, 'Санкт-Петербург', 'kiseleva_yulya@mail.ru', '8-905-6322320')
get_person(name='Joe', surname='Smith', birth_year=1983, city='New York', email='joesmith@gmail.com', phone='+19992222222')

# Можно реализовать через kwargs:
def get_person_new(**kwargs):
    '''
    Функция выводит на экран данные о пользователе, которые вводятся в виде именованных аргументов
    :param kwargs: str, ключ - наименование параметров, которые мы хотим записать, значение - персональные данные пользователя
    :return: Вывод всех значений с наименованиями в строку
    '''
    for param, user_data in kwargs.items():
        print(f'{param}: {user_data}', end=", ")

get_person_new(Name="Joe", Surname="Smith", Birth_year=1983, City="New York", Email="joesmith@gmail.com", Phone="+19992222222")