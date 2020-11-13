def func(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        return 'No / 0'


a = int(input('Первое число'))
b = int(input('Второе число'))
print(func(a, b))
