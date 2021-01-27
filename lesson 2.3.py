user_month = int(input('Введите месяц: '))
print('Через list:')
season = ['Зима', 'Весна', 'Лето', 'Осень']
if user_month < 3 or user_month == 12:
    print(season[0])
elif user_month < 6:
    print(season[1])
elif user_month < 9:
    print(season[2])
elif user_month < 12:
    print(season[3])

print('Через dict:')
season_dict = {'Winter': 'Зима', 'Spring': 'Весна', 'Summer': 'Лето', 'Autumn': 'Осень'}
if user_month < 3 or user_month == 12:
    print(season_dict['Winter'])
elif user_month < 6:
    print(season_dict['Spring'])
elif user_month < 9:
    print(season_dict['Summer'])
elif user_month < 12:
    print(season_dict['Autumn'])
