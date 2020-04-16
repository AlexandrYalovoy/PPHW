# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

def read_file(name_file):
    """
    код чтения из файла для возврата строкой содержимого файла
    :param name_file: имя файла который будем читать. Пример ('text_4.txt')
    :return: возврашает содержимое файла строкой
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(name_file, text):
    """
    записи в файл с его перезаписыванием и возможностью создать файл
    :param name_file: имя файла в который будем писать или создавать и писать. Пример ('text_4_translate.txt')
    :return: возврашает содержимое файла строкой
    """
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(text)


# Словарь с переводами слов. Про гугл я не умею мне пока эти задачи подалеть надо
translate_dict = {'One': 'Один',
                  'Two': 'Два',
                  'Three': 'Три',
                  'Four': 'Четыре',}

file_text_str = read_file('text_4.txt')

for key, value in translate_dict.items():
    file_text_str = file_text_str.replace(key, value)

print(file_text_str)

write_file('text_4_translate.txt', file_text_str)