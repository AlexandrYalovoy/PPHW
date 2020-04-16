# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


with open('text_6.txt', 'r', encoding='utf-8') as file:
    result_dict = {}
    while True:
        line_list = file.readline().split()
        if not line_list:
            break
        key = line_list.pop(0)[:-1]
        list_numbers = []
        for i_str in line_list:
            list_number = []
            for index in range(0, len(i_str)):
                if i_str[index].isdigit():
                    list_number.append(i_str[index])
            if list_number != []:
                number = float(''.join(list_number))
                list_numbers.append(number)
        value = sum(list_numbers)
        result_dict[key] = value
    print(result_dict)
