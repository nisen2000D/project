def division():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    try:
        ans = num_1 / num_2
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    else:
        return ans


print(division())
