x = int(input('Введите положительно число: '))
if x <= 0:
    print('Нужно было ввести положительное число')
else:
    y = int(input('Введите отрицателье число: '))
    if y >= 0:
        print('Нужно было ввести отрицательное число')
    else:

        def my_func(x, y):
            return x ** y


        print(my_func(x, y))
