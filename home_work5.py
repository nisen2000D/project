revenue = int(input('Выручка: '))
cost = int(input('Издержки:'))
income = revenue - cost

if revenue > cost:
    print('Прибыль')
    prof = income / revenue
    print(f'Рентабельность {prof}')
else:
    print('Убыток')

num = int(input('Численность сотрудников: '))
inc = income / num
print(f'Прибыль на 1 сотрудника: {inc}')
