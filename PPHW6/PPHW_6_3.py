# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker_tab_246000:
    # Атребуты
    name = 'Кутуша'
    surname = 'Штуша'
    position = 'Страшный зверь'
    wage = 50000
    bonus = 50000
    _income = {'wage': wage, 'bonus': bonus}
    currency = '\u20bd'
    __render_services = ['Грабежи', 'Разбой', 'Угрозы', 'Вымогательства']


class Position(Worker_tab_246000):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __get_render_services(self):
        return ((', '.join(self._Worker_tab_246000__render_services)).lower()).capitalize()


villain_woods = Position()

print(f'У сотрудника леса {villain_woods.get_full_name()} доход в месяц составил {villain_woods.get_total_income()} '
      f'{villain_woods.currency}.\n'
      f'Должность в лесу: {villain_woods.position}.\n'
      f'Оказываемые услуги лесу: {villain_woods._Position__get_render_services()}.')
