# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.num_complex = complex(a, b)

    def __add__(self, other):
        return complex(self.num_complex) + complex(other.num_complex)

    def __mul__(self, other):
        return complex(self.num_complex) * complex(other.num_complex)

    def __str__(self):
        return str(self.num_complex)


one_complex = ComplexNumber(1, 2)
print(f'Первое комплексное число {one_complex}.')
two_complex = ComplexNumber(3, -1)
print(f'Второе комплексное число {two_complex}.')
add_complex = one_complex + two_complex
print(f'Сумма комплексных чисел {add_complex}.')
mul_complex = one_complex * two_complex
print(f'Произведение коплексных чисел {mul_complex}.')