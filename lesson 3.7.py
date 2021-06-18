user_word = input('Введите строку с маленькой буквы и латинским алфавитом: ')
latin = 'qwertyuiopasdfghjklzxcvbnm'


def int_func(user):
    for el in range(len(user)):
        for lat in range(len(latin)):
            if user[el] == latin[lat] and user[el] == latin[lat].lower():
                print(user.title())
                break
        else:
            print('Строка была введена с большой буквы и/или не латинским алфавитом')
            break
        break


int_func(user_word)
