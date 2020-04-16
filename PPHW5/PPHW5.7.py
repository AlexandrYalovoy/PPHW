# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

with open('text_7.txt', 'r', encoding='utf-8') as file:
    result_dict = {}
    all_dict_firm = {}
    while True:
        line_list = file.readline().split()
        if not line_list:
            break
        line_list[0] = '"' + line_list[0] + '"'
        key_list = []
        for i in range(0, 2):
            key_list.append(line_list[i])
        key = ' '.join(reversed(key_list))
        average_firm = float(line_list[2]) - float(line_list[3])
        if average_firm > 0:
            result_dict[key] = average_firm
        all_dict_firm[key] = average_firm

    score = 0
    average_all_list = []
    average_dict = {}
    for key_2, value in result_dict.items():
        score += 1
        average_all_list.append(value)
    average_profit = sum(average_all_list) / score

    average_dict['average_profit'] = average_profit

    result_list = []
    result_list.append(all_dict_firm)
    result_list.append(average_dict)

    print(result_list)

# сохранение в файл
with open('JSON_PPHW5.7.json', 'w', encoding='utf-8') as file:
    json.dump(result_list, file)

# чтение с принтом для простоты проверки
with open('JSON_PPHW5.7.json', 'r', encoding='utf-8') as file:
    open_result_list_json = json.load(file)
    print(open_result_list_json)