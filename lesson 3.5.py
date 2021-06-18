def my_sum():
    sum_res = 0
    i = False
    while i == False:
        number = input('Введите числа или q для выхода: ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                i = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма чисел: {sum_res}')
    print(f'Итого сумма чисел: {sum_res}')


my_sum()
