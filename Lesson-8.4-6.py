# Задача - описать систему учета оргтехники на складе и работы самого склада.
# Объекты: оргтехника разных типов, склады, покупатели
# Классы: Склад, Оргтехника, Принтер, Сканер, Копир, Покупатель
# Атрибуты классов:
# Склад - размеры склада, теплый/холодный, количество сотрудников склада, количество единиц погрузочной техники.
# Оргтехника - номер инвентарный, название, бренд, цена, место на складе, счетчик созданных экземпляров
# Принтер - скорость печати, цветность, двухсторонняя печать, USB, WiFi, счетчик созданных экземпляров
# Сканер - скорость сканирования, потоковое сканирование, формат, счетчик созданных экземпляров
# Копир - скорость копирования, автоподача, счетчик созданных экземпляров
# Покупатели - наименование, список купленных товаров
# Методы:
# Склад - расчет вместимости склада, прием товара на склад, отгрузка покупателю
# Оргтехника, принтер, сканер, копир - подсчет созданных экземпляров
# Покупатели - приобретение товаров

class Warehouse:
    def __init__(self, name, lenght, width, height, is_warm, staff, equipment):
        self.name = name
        self.length = lenght
        self.width = width
        self.height = height
        self.is_warm = is_warm
        self.staff = staff
        self.equipment = equipment
        self.nomenclature = {}

    def wh_volume(self):
        '''
        Рассчитывается объем/размер склада
        :return: int. Объем в кубических метрах
        '''
        wh_volume = self.length * self.width * self.height
        return wh_volume

    def to_take_on_balance(self, new_unit):
        """
        Прием товара на склад. Формирует словарь из оборудования на складе, добавляет новый элемент в словарь
        :param new_unit: dict. Содержит информацию о добавляемой или изменяемой единице. Словарь вида:
        номер по номенклатуре: кол-во
        :return: dict. Cписок хранимых единиц товаров в виде словаря
        """
        self.nomenclature.update(new_unit)
        return self.nomenclature

    def to_ship(self, customer, **new_goods):
        """
        Отгрузка покупателю или перемещение между складами. Убирает товар из списка наличия и добавляет в список покупок
        покупателя.
        :param customer: Покупатель, которому производится отгрузка
        :param new_goods: список отгружаемых товаров и их количество
        :return:
        """
        customer.to_buy(**new_goods)
        print(f'Клиенту {customer.name} были отгружены следующие товары: {customer.shipped_goods}')
        self.nomenclature = {k: self.nomenclature[k] - customer.shipped_goods[k] for k in customer.shipped_goods}
        print(f'Товары в наличии после отгрузки покупателю {customer.name} - {self.nomenclature}')

class OfficeEquipment:
    office_equipment_count = 0
    def __init__(self, inventory_number, name, brand, price, warehouse_place):
        self.inventory_number = inventory_number
        self.name = name
        self.brand = brand
        self.price = price
        self.warehouse_place = warehouse_place
        OfficeEquipment.office_equipment_count += 1

    @staticmethod
    def print_num_of_instance():
        print(f'Количество созданных единиц оргтехники в классе {__class__.__name__} - {OfficeEquipment.office_equipment_count}')

class Printer(OfficeEquipment):
    printer_count = 0
    def __init__(self, inventory_number, name, brand, price, warehouse_place, printing_speed, color, has_usb, has_wifi,
                 two_side_print):
        super().__init__(inventory_number, name, brand, price, warehouse_place)
        self.printing_speed = printing_speed
        self.color = color
        self.has_usb = has_usb
        self.has_wifi = has_wifi
        self.two_side_print = two_side_print
        Printer.printer_count += 1

    @staticmethod
    def print_num_of_instance():
        print(f'Количество созданных единиц оргтехники в классе {__class__.__name__} - {Printer.printer_count}')

class Scaner(OfficeEquipment):
    scaner_count = 0
    def __init__(self, inventory_number, name, brand, price, warehouse_place, scaning_speed, streaming_scan, size):
        super().__init__(inventory_number, name, brand, price, warehouse_place)
        self.scaning_speed = scaning_speed
        self.streaming_scan = streaming_scan
        self.size = size
        Scaner.scaner_count += 1

    @staticmethod
    def print_num_of_instance():
        print(f'Количество созданных единиц оргтехники в классе {__class__.__name__} - {Scaner.scaner_count}')

class Copier(OfficeEquipment):
    copier_count = 0
    def __init__(self, inventory_number, name, brand, price, warehouse_place, copy_speed, autom_pap_delivery):
        super().__init__(inventory_number, name, brand, price, warehouse_place)
        self.copy_speed = copy_speed
        self.autom_pap_delivery = autom_pap_delivery
        Copier.copier_count += 1

    @staticmethod
    def print_num_of_instance():
        print(f'Количество созданных единиц оргтехники в классе {__class__.__name__} - {Copier.copier_count}')

class Customer:
    def __init__(self, name):
        self.name = name
        self.shipped_goods = {}

    def to_buy(self, **new_goods):
        """
        Метод отражает приобретение покупателем товара. Принимает в качестве аргумента словарь вида: наименование: кол-во
        :param new_good: dict. Отгруженные товары
        :return: dict.
        """
        self.shipped_goods.update(**new_goods)


warehouse1 = Warehouse('Склад оргтехники', 10, 15, 5, True, 5, 3)
printer1 = Printer(1, 'принтер', 'HP', 15000, '23B', 28, True, True, False, True)
printer2 = Printer(4, 'принтер', 'Epson', 10000, '24B', 25, False, False, False, False)
printer3 = Printer(5, 'принтер', 'Samsung', 25000, '25B', 32, True, True, True, True)
scaner1 = Scaner(2, 'сканер', 'Canon', 10000, '18A', 15, False, 'A4')
scaner2 = Scaner(3, 'сканер', 'HP', 11000, '19A', 10, True, 'A5, A4')

OfficeEquipment.print_num_of_instance()
Printer.print_num_of_instance()
Scaner.print_num_of_instance()
Copier.print_num_of_instance()
print(warehouse1.to_take_on_balance({'Принтер': Printer.printer_count, 'Сканер': Scaner.scaner_count, 'Копир': Copier.copier_count}))

customer1 = Customer('ООО Ромашка')
warehouse1.to_ship(customer1, Принтер=1, Сканер=1)

