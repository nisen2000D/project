user_sec = int(input('Введите время в секундах: '))

minute = user_sec // 60
hour = minute // 60
second = user_sec % minute

print(f'{hour}:{minute}:{second}')
