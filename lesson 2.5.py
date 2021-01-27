my_list = [3, 4, 6, 1, 9]
i = 0
while True:
    user_num = int(input('Введите число: '))
    if i > 0:
        my_list.pop()
    my_list.append(user_num)
    print(sorted(my_list, reverse=True))
    i += 1
