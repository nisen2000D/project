name = input('Введите имя: ')
surname = input('Введите фамилию: ')
date = input('Дата рождения: ')
city = input('Город проживания: ')
email = input('Email: ')
number = input('Номер телефона: ')


def my_func(**kwargs):
    return kwargs


print(
    my_func(Имя_пользователя=name, фамилия=surname, дата_рождения=date, город_проживания=city, email_пользователя=email,
            номер_телефона=number))
