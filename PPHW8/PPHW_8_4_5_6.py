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
    warehouse_office_equipment = defaultdict(dict)


class CompanyDivision(Warehouse):
    company_division = defaultdict(dict)

    # Проперти запихано просто для того чтоб было, какого то смысла и удоства я в нем не вижу.
    @property
    def take_office_equipment(self):
        print('На скдаде имеются следующие группы оргтехники:')
        list_group_equipment = []
        for num, key in enumerate(self.warehouse_office_equipment.keys(), 1):
            print(f'{num}) {key}')
            list_group_equipment.append(key)
        while True:
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




class OfficeEquipment(Warehouse):
    def __init__(self, device_name, serial_number, model, device_type='etc'):
        self.device_name = device_name
        self.serial_number = serial_number
        self.model = model
        self.device_type = device_type
        self.device_info_dict = {self.serial_number: [self.device_type, self.device_name, self.model]}

    def add_warehouse(self):
        self.warehouse_office_equipment[self.device_type][self.serial_number] = self.device_info_dict[self.serial_number]






class Scanner(OfficeEquipment):
    def __init__(self, device_name, serial_number, model, device_type='Scanner'):
        super().__init__(device_name, serial_number, model, device_type)


class Printer(OfficeEquipment):
    def __init__(self, device_name, serial_number, model, print_type):
        super().__init__(device_name, serial_number, model)
        self.device_type = 'Printer'
        self.print_type = print_type
        self.device_info_dict = {serial_number: [self.device_type, self.device_name, self.model, self.print_type]}

class Xerox(OfficeEquipment):
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

company_division.take_office_equipment

