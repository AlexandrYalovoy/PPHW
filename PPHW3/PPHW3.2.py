# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def users_info(name, family, years_old, city_residence, e_mail, phone):
    return f'{name}, {family}, {years_old}, {city_residence}, {e_mail}, {phone}'


print(users_info(family='Дудка', name='Gurgen', city_residence='Hasavurt', years_old=1988, e_mail='DG@mail.ru',
                 phone='+79069069006'))
