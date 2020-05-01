# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

from collections import defaultdict


class Warehouse:
    """Класс "Склад" который хранит технику.
    Склад по моему представлению должен просто хранить технику, а передовать и брать её должны подразделенеия
    дабы не пладить бюррократию и формализм.
    Информация храниться в многомерном словаре типа:
    Укрупненная группа техники: Серийный номер: [описание техники]
    {'Scanner': {'QR5445246Sd': ['Scanner', 'CANON CanoScan', 'LiDE 400']},
    'Xerox': {'ddfre3356': ['Xerox', 'Xerox AltaLink', 'C8070'],
            'Qde34543': ['Xerox', 'Xerox WorkCentre', '3335']},
    'Printer': {153654: ['Printer', 'CANON i-SENSYS', 'LBP663Cdw', 'Лазерный цветной']}})
    """
    warehouse_office_equipment = defaultdict(dict)


class CompanyDivision(Warehouse):
    """
    Класс опписывающий подразделение компании.
    Может брать технику со склада, обратно передавать ее не может, потому что на склоаде должны храниться только
    новые экземпляры не бывшие в употреблении.
    Тип хранения техники аналог "Склад"
    """
    company_division = defaultdict(dict)

    # Проперти запихано просто для того чтоб было, какого то смысла и удоства я в нем не вижу.
    @property
    def take_office_equipment(self):
        """
        Функция которая позволяет забрать технику со склада подразделением.
        Ничего не возврашает. Перемещает выбранную технику из словаря warehouse_office_equipment
        в словарь company_division.
        :return: Ничего не возвоашает.
        """

        print('На скдаде имеются следующие группы оргтехники:')
        list_group_equipment = []
        for num, key in enumerate(self.warehouse_office_equipment.keys(), 1):
            print(f'{num}) {key}')
            list_group_equipment.append(key)
        while True:
            # Валидация данных от пользователя
            try:
                num_group = int(input('Введите номер группы для просмотра - '))
            except ValueError:
                print('Введите число!')
            else:
                if num_group > 0 and num_group <= (len(list_group_equipment)):
                    num_group -= 1
                    name_group = list_group_equipment[num_group]
                    break
        print(f'\nВ группе {name_group} содержится следующая техника:')
        list_item_group_equipment = []
        for num_1, key_1 in enumerate(self.warehouse_office_equipment[name_group].keys(), 1):
            print(f'{num_1}) Серийный номер ({key_1}) устройство {self.warehouse_office_equipment[name_group][key_1]}')
            list_item_group_equipment.append(key_1)
        while True:
            # Валидация данных от пользователя (Внедрение функцйии для валидации излишне усложнила код, и я от нее
            # избавился, ибо было без пол литра не разобраться. некое дублирование кода упростило понимание и позволило
            # отсылаться без проблем ко всем переменным в методе внутри метода.)
            try:
                num_item_group = int(input('Введите номер устройства для получения - '))
            except ValueError:
                print('Введите число!')
            else:
                if num_item_group > 0 and num_item_group <= (len(list_item_group_equipment)):
                    num_item_group -= 1
                    name_item_group = list_item_group_equipment[num_item_group]
                    break
        print(f'\nВыбрано устройство {self.warehouse_office_equipment[name_group][name_item_group]} '
              f'серийный номер ({name_item_group}).')
        while True:
            user_confirmation = input('\nДля того что бы забрать устройтсво введите "Да/Д/Y", '
                                      'для отказа "Нет/Н/N" - ').lower()
            if user_confirmation == 'да' or user_confirmation == 'д' or user_confirmation == 'y':
                self.company_division[name_group][name_item_group] = self.warehouse_office_equipment[name_group][
                    name_item_group]
                del self.warehouse_office_equipment[name_group][name_item_group]
                if self.warehouse_office_equipment[name_group] == {}:
                    del self.warehouse_office_equipment[name_group]
                break
            elif user_confirmation == 'нет' or user_confirmation == 'н' or user_confirmation == 'n':
                break


class OfficeEquipment(Warehouse):
    """
    Класс описывающий новую тенику и позволяющий передать ее на склад.
    Так же позволяет создавать всякую разную технику с шаблонным описанием
    Является родительским классом для типовой распространненой техники такой как
    Scanner, Printer, Xerox.
    """
    def __init__(self, device_name, serial_number, model, device_type='etc'):
        self.device_name = device_name
        self.serial_number = serial_number
        self.model = model
        self.device_type = device_type
        self.device_info_dict = {self.serial_number: [self.device_type, self.device_name, self.model]}

    def add_warehouse(self):
        """
        Позволяет передать новый экземпляр техники на склад до востребования.
        :return: Ничего не возрашает.
        """
        self.warehouse_office_equipment[self.device_type][self.serial_number] = self.device_info_dict[
            self.serial_number]


class Scanner(OfficeEquipment):
    """
    Класс создания нового Сканера
    Может передавать на склад
    """
    def __init__(self, device_name, serial_number, model, device_type='Scanner'):
        super().__init__(device_name, serial_number, model, device_type)


class Printer(OfficeEquipment):
    """
    Класс создания нового принтера
    Может передавать на склад
    """
    def __init__(self, device_name, serial_number, model, print_type):
        super().__init__(device_name, serial_number, model)
        self.device_type = 'Printer'
        self.print_type = print_type
        self.device_info_dict = {serial_number: [self.device_type, self.device_name, self.model, self.print_type]}


class Xerox(OfficeEquipment):
    """
    Коласс создания нового ксерокса, как фирмы ксерокс так и нет но запихает их всех под общий ключ 'Xerox'
    Может передавать на склад
    """
    def __init__(self, device_name, serial_number, model, device_type='Xerox'):
        super().__init__(device_name, serial_number, model, device_type)


warehouse = Warehouse()

company_division = CompanyDivision()

print('Обозначим принтер')
pinter = Printer('CANON i-SENSYS', 153654, 'LBP663Cdw', 'Лазерный цветной')
print(pinter.device_info_dict)
print()

print('Обозначим сканер')
scanner = Scanner('CANON CanoScan', 'QR5445246Sd', 'LiDE 400')
print(scanner.device_info_dict)
print()

print('Обозначим ксерокс')
xerox = Xerox('Xerox AltaLink', 'ddfre3356', 'C8070')
print(xerox.device_info_dict)
print()

print('Обозначим ксерокс №2')
xerox2 = Xerox('Xerox WorkCentre', 'Qde34543', '3335')
print(xerox2.device_info_dict)
print()

print('Отправим на склад ксерокс')
scanner.add_warehouse()
print(warehouse.warehouse_office_equipment)
print()
print('Отправим на склад ксерокс')
xerox.add_warehouse()
print(warehouse.warehouse_office_equipment)
print()
print('Отправим на склад ксерокс №2')
xerox2.add_warehouse()
print(warehouse.warehouse_office_equipment)
print()
print('Отправим на склад принтер')
pinter.add_warehouse()
print(warehouse.warehouse_office_equipment)

print(warehouse.warehouse_office_equipment.keys())
print(warehouse.warehouse_office_equipment['Xerox'].keys())
print(warehouse.warehouse_office_equipment['Xerox'].items())
print()
print('Пусть подразделение возьмет какую то единицу техники')
company_division.take_office_equipment
print()
print('Технтка в подразделении')
print(company_division.company_division)
print()
print('Техника которая осталась на складе')
print(warehouse.warehouse_office_equipment)
