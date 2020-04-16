# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества
# строк, количества слов в каждой строке.


def read_file(name_file):
    """
    код чтения из файла для вывода содержимого для простой проверки
    :param name_file: имя файла который будем читать. Пример ('PPHW5.2.txt')
    :return: выводит все содержимое файла
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        print(file.read())


def quantity_lines_in_file(name_file):
    """
    Принтует количество строк в файле
    :param name_file: имя файла который будем читать. Пример ('PPHW5.2.txt')
    :return: возврашает количество строк в виде числа
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        score = 0
        while True:
            content = file.readline()
            if not content:
                break
            score += 1
        return score


def quantity_word_in_file(name_file):
    """
    Получает количество слов в файле
    :param name_file: имя файла который будем читать. Пример ('PPHW5.2.txt')
    :return: возврашает количество слов в файле в виде числа
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        check_word_sum_list = []
        while True:
            content = file.readline()
            if not content:
                break
            check_word_sum_list.extend(content.split())
        return len(check_word_sum_list)


def quantity_symbols_in_file(name_file):
    """
    Получает количество символов в файле без пробелов
    :param name_file: имя файла который будем читать. Пример ('PPHW5.2.txt')
    :return: возврашает количество символов в файле в виде числа
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        content = file.read()
        content = content.split()
        content = ''.join(content)
        return len(content)


def quantity_el_in_file(name_file):
    """
    получает количество элементов в файле c пробелами и без операторов новых строк
    :param name_file: имя файла который будем читать. Пример ('PPHW5.2.txt')
    :return: возврашает количество элементов в файле в виде числа по условию
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        str_test = ''
        while True:
            content = file.readline()
            if not content:
                break
            str_test += content
        return len(str_test.replace('\n', ''))


def quantity_element_in_file(name_file):
    """
    Количество элементов в файле c пробелами и операторами новых строк
    :param name_file: имя файла который будем читать. Пример ('PPHW5.2.txt')
    :return: возврашает количество элементов в файле в виде числа по условию
    """
    with open(name_file, 'r', encoding='utf-8') as file:
        content = file.read()
        return len(content)


def str_info_for_text_file(name_file):
    print(f'Количество строк в файле - {quantity_lines_in_file(name_file)};\n'
          f'Количество слов в файле - {quantity_word_in_file(name_file)};\n'
          f'Количество символов в файле без пробелов и операторов новых строк - {quantity_symbols_in_file(name_file)};\n'
          f'Количество элементов в файле c пробелами и без операторов новых строк - {quantity_el_in_file(name_file)};\n'
          f'Количество элементов в файле c пробелами и операторами новых строк - {quantity_element_in_file(name_file)}.')


# Есть легкий проверочный файл 'PPHW5.2.1.txt'
read_file('PPHW5.2.txt')
print()
str_info_for_text_file('PPHW5.2.txt')
print()
