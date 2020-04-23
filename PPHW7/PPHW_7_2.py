# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто
# и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Base_clothes_abstract(ABC):
    @abstractmethod
    def quantity_cloth_in_model(self):
        pass


class Coat(Base_clothes_abstract):
    def __init__(self, quantity_cloth=0, coat_quantity=0, name_coat='"Костюм"', sizes_coat=[]):
        self.quantity_cloth = quantity_cloth
        self.coat_quantity = coat_quantity
        self.name_coat = name_coat
        self.sizes_coat = sizes_coat

    def quantity_cloth_in_model(self, *size):
        for i in size:
            self.sizes_coat.append(i)
            self.quantity_cloth += (i / 6.5) + 0.5
        self.quantity_cloth = round(self.quantity_cloth, 2)
        self.coat_quantity = len(self.sizes_coat)
        return self.quantity_cloth


class Suit(Base_clothes_abstract):
    def __init__(self, quantity_cloth=0, suit_quantity=0, name_suit='"Костюм"', sizes_suit=[]):
        self.quantity_cloth = quantity_cloth
        self.suit_quantity = suit_quantity
        self.name_suit = name_suit
        self.sizes_suit = sizes_suit

    def quantity_cloth_in_model(self, *height):
        for i in height:
            self.sizes_suit.append(i)
            self.quantity_cloth += (2 * i) + 0.3
        self.quantity_cloth = round(self.quantity_cloth, 2)
        self.suit_quantity = len(self.sizes_suit)
        return self.quantity_cloth


class Clothes(Coat, Suit):
    all_quantity_cloth = 0

    def sum_quantity_cloth(self, *quantity_cloth):
        for i in quantity_cloth:
            self.all_quantity_cloth += i
        return self.all_quantity_cloth

    @property
    def info_print(self):
        print(f'Для пошива партии необходимо {self.all_quantity_cloth} пагонных метров полотна.\n')


coat = Coat()
suit = Suit()
clothes = Clothes()

coat.quantity_cloth_in_model(40, 42, 44, 46, 48, 50)
suit.quantity_cloth_in_model(1.64, 1.70, 1.80, 1.82, 1.86, 1.90)

clothes.sum_quantity_cloth(coat.quantity_cloth, suit.quantity_cloth)


clothes.info_print