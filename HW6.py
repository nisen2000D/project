my_list = []
i = 1
while i < 4:
    name = input('Введите название товара: ')
    price = int(input('Введите цену: '))
    quantity = int(input('Введите количество: '))
    unit = (input('Введите единицу измерения: '))

    my_list.append((i, {'название': f'{name}', 'цена': price, 'количество': quantity, 'eд': f'{unit}'}))
    i += 1
for el in my_list:
    print(el)

goods = int(input("Введите количество товара "))
n = 1
my_dict = []
my_list = []
my_goods = {}
while n <= goods:
    my_dict = dict({'название': input("Введите название: "), 'цена': input("Введите цену: "),
                    'количество': input('Введите количество '), 'eд': input("Введите единицу измерения: ")})

    my_goods = dict(
        {'название': my_dict.get('название'), 'цена': my_dict.get('цена'), 'количество': my_dict.get('количество'),
         'ед': my_dict.get('ед')})
    my_list.append((n, my_dict))
    n += 1
for i in my_list:
    print(i)

