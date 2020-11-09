n = 0
my_list = []
score = 0
while n != 1:
    my_list.append(input('Введите число'))
    n = int(input('Введите 1,если хотите прекратить'))
    score = score + 1
n = 0
while True:
    if score // 2 == 0:
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n = n + 2
    else:
        a = my_list.pop(-1)
        my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
        n = n + 2
        my_list.append(a)
print(my_list)
#не выводиться принт