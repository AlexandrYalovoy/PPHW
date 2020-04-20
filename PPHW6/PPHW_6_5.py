# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.


class Stationery:
    title = 'Канцелярские принадлжености'

    def draw(self):
        print(F'Запуск отрисовки с помошью "{self.title}".')


class Pen(Stationery):
    title = 'Pen'


class Pencil(Stationery):
    title = 'Pencil'


class Handle(Stationery):
    title = 'Handle'


pen = Pen()

pencil = Pencil()

handle = Handle()

pen.draw()

pencil.draw()

handle.draw()