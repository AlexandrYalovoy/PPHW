# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class DivisionByZero(Exception):
    def __str__(self):
        return 'На ноль делить нельзя!'


def division(private, divider):
    try:
        if divider == 0:
            raise DivisionByZero()
        return float(private) / float(divider)
    except ValueError:
        return 'Вводить можно только числа'
    except DivisionByZero as i:
        return i


print(division(5, 5))

print(division(5, 's'))

print(division(5, 0))
