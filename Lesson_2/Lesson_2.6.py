# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

product_list = []
number_of_products = int(input("Введите количество товаров: "))
cycle_counter = 1
key_1 = "Название"
key_2 = "Цена"
key_3 = "Количество"
key_4 = "Ед.измерения"
name_list = []
price_list = []
quantity_list = []
unit_list = []

while cycle_counter <= number_of_products:
    number = int(input('Введите номер товара: '))
    name = input(f"Введите {key_1} товара: ")
    price = float(input(f"Введите {key_2} товара: "))
    quantity = int(input(f"Введите {key_3} товара: "))
    unit = input(f"Введите {key_4}: ")
    products = {key_1: name, key_2: price, key_3: quantity, key_4: unit}
    my_tuple = (number, products)
    product_list.append(my_tuple)
    name_list.append(name)
    price_list.append(price)
    quantity_list.append(quantity)
    unit_list.append(unit)
    cycle_counter += 1
name_dict = {key_1: name_list}
price_dict = {key_2: price_list}
quantity_dict = {key_3: quantity_list}
unit_dict = {key_4: unit_list}
print(product_list)
print(name_dict)
print(price_dict)
print(quantity_dict)
print(unit_dict)


