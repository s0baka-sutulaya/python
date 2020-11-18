from itertools import count
from math import factorial


def gen():
    for i in count(1):
        yield factorial(i)


x = 1
for k in gen():
    if x != 20:
        print('Факториал числа', x, '=', k)
        x += 1
    else:
        break
