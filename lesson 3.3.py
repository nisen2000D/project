num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))
numbers = [num1, num2, num3]


def my_func():
    ind = numbers.index(min(numbers))
    del numbers[ind]
    return numbers


print(my_func())
