# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class MyDate:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_num(cls, date1):
        num1, num2, num3 = map(int, date1.split('-'))
        print(num1, num2, num3)
        print(type(num1), type(num2), type(num3))

    @staticmethod
    def date_valid(date2):
        day, month, year = map(int, date2.split('-'))
        if day in range(1, 32) and month in range(1, 13) and year in range(1900, 2022):
            print('Дата введена правильно')
        else:
            print('Дата введена с ошибкой!')

MyDate.date_num('03-03-2003')
MyDate.date_valid('03-03-2006')
