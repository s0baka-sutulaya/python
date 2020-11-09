my_list = input('Введите слова через пробел')
for index, word in enumerate(my_list.split(), 1):
    print(index, word[:10])



