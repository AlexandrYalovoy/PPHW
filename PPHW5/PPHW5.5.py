# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def write_file(name_file, text):
    """
    записи в файл с его перезаписыванием и возможностью создать файл
    :param name_file: имя файла в который будем писать или создавать и писать. Пример ('text_4_translate.txt')
    :return: возврашает содержимое файла строкой
    """
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(text)


def read_file(name_file):
    """
    код чтения из файла для возврата строкой содержимого файла
    :param name_file: имя файла который будем читать. Пример ('text_4.txt')
    :return: возврашает содержимое файла строкой
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read()


text_for_write = '5 5 5 5 5 5 5 5'

write_file('PPHW5.5_number.txt', text_for_write)

text_file_str = read_file('PPHW5.5_number.txt')

text_list = text_file_str.split()
text_list_float = []
for i in text_list:
    if i.isdigit():
        text_list_float.append(float(i))

print(f'Сумма чисел в файле {sum(text_list_float)}')