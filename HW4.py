my_str = input("Введите строку: ")
my_word = []
num = 1
for i in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [i]}")
        num += 1
    else:
        print(f" {num} {my_word [i] [0:10]}")
        num += 1
