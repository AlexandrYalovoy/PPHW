# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

from copy import deepcopy


class Matrix:
    result_matrix = []

    def __init__(self, number_lines=3, number_items_lines=3, auto=False, auto_matrix=[[5, 5], [5, 5], [5, 5]]):
        """
        Конструктор позволяющий запросить матрицу у пользователя, любой длины любой ширины.
        По умлочанию матрица 3х3.
        Можно принять авто матрицу если параметр auto=True, а так же передать автоматрицу, при этом у пользователя
        ничего спрашиваться не будет.
        :param number_lines: Количество строк в матрицу (Ширина)
        :param number_items_lines: Количество элементов в строке матрицы (Длина)
        :param auto: False или True в зависимости нужна авто матрица или нет
        :param auto_matrix: Матрица по умолчанию по умолчанию
        """
        if auto:
            self.result_matrix = auto_matrix
            return  # посяните правильно ли так тормазить реурном, мне кажется не верно но как я не придумал
        for lines in range(0, number_lines):
            line_list = []
            for item in range(0, number_items_lines):
                while True:
                    item_line = input(f'Строка {lines + 1} позиция {item + 1}, введите число - ')
                    if item_line.isdigit():
                        item_line = int(item_line)
                        line_list.append(item_line)
                        break
                    else:
                        print('Принимается только число!')
            self.result_matrix.append(line_list)

    def __str__(self):
        """
        При запросе принт возврашает матрицу списком
        :return: возврашает матрицу списком
        """
        str_matrix_result = ''
        for line in range(0, len(self.result_matrix)):
            str_matrix_result += ' '.join(map(lambda item: str(item), self.result_matrix[line]))
            if line < len(self.result_matrix) - 1:
                str_matrix_result += '\n'
        return str_matrix_result

    def __add__(self, other):
        """
        Складывает 2 матрицы. Если матрицы разного размера то преобразует к одинаковому порядку
        :param other: другая матрица
        :return: возврашает список(матрицу) с результатом сложения
        """

        def add_lines(matrix_list):
            """
            Добавляет строку в матрицу для преобразования матрицы к одному порядку.
            :param matrix_list: матрица которая будет проверяться на наличие строки
            :return: Ничего не возврашает просто добавляет строку в матрицу.
            """
            try:
                check_index = matrix_list[lines]
            except IndexError:
                matrix_list.append([])

        def add_item_in_lines(matrix_list):
            """
            Добавляет в строку значение "0"  для преобразования матрицы к одному порядку.
            :param matrix_list:матрица которая будет проверяться на наличие элемента строки
            :return: ничего не возврашает просто добовляет в конец строки "0"
            """
            try:
                check_index = matrix_list[lines][item]
            except IndexError:
                matrix_list[lines].append(0)

        one_matrix = deepcopy(self.result_matrix)
        two_matrix = deepcopy(other.result_matrix)
        sum_matrix = []

        for lines in range(0, len(one_matrix) if len(one_matrix) >
                                                 len(two_matrix) else len(two_matrix)):
            sum_line_item = []

            add_lines(one_matrix)
            add_lines(two_matrix)

            for item in range(0, len(one_matrix[lines]) if len(one_matrix[lines]) >
                                                           len(two_matrix[lines]) else len(two_matrix[lines])):
                add_item_in_lines(one_matrix)
                add_item_in_lines(two_matrix)
                sum_item = one_matrix[lines][item] + two_matrix[lines][item]
                sum_line_item.append(sum_item)
            while True:
                try:
                    if len(sum_line_item) == len(sum_matrix[0]):
                        break
                    else:
                        sum_line_item.append(0)
                        if len(one_matrix[lines]) < len(sum_line_item):
                            one_matrix[lines].append(0)
                        if len(two_matrix[lines]) < len(sum_line_item):
                            two_matrix[lines].append(0)
                except IndexError:
                    break

            sum_matrix.append(sum_line_item)
        return sum_matrix


matrix_1 = Matrix(auto=True, auto_matrix=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
print(matrix_1)
print('+')

matrix_2 = Matrix(auto=True, auto_matrix=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(matrix_2)
print('=')

print(matrix_1 + matrix_2)

matrix_3 = matrix_1 + matrix_2

result_sum_matrix = Matrix(auto=True, auto_matrix=matrix_3)
print('А если красиво то:')
print(result_sum_matrix)
