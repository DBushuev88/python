"""
    name = input('enter name')
    surname = input('enter surname')
    year = int(input('enter year'))
    city = input('enter city')
    email = input('enter email')
    telephone = input('input telephone')
"""


def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Bushuev', name='Dmitry', year='1988', city='Moscow', email='mylo@mail.ru',
              telephone='8-999-777-66-55'))
