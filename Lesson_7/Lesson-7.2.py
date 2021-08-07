# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    def tissue_consumption(self):
        coat_tiss_cons = self.size / 6.5 + 0.5
        return coat_tiss_cons

class Suit(Clothes):
    def __init__(self, height):
        self.height = height

    def tissue_consumption(self):
        suit_tiss_cons = self.height * 2 + 0.3
        return suit_tiss_cons

class TissueConsumption:
    def __init__(self):
        self.clothes_list = []

    def add_coat(self, size):
        self.clothes_list.append(Coat(size).tissue_consumption())

    def add_suit(self, height):
        self.clothes_list.append(Suit(height).tissue_consumption())

    def total_tissue_consumption(self):
        total_tissue_consumption = sum(self.clothes_list)
        return total_tissue_consumption

tc1 = TissueConsumption()
tc1.add_coat(52)
tc1.add_coat(48)
tc1.add_suit(175)
print(tc1.total_tissue_consumption())


