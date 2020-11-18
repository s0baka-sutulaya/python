from functools import reduce


def pr(var_1, var_2):
    return var_1 * var_2


my_list = [i for i in range(100, 1001, 2)]
answer = reduce(pr, my_list)
print(answer)

