def summing(var_1, var_2, var_3):
    if var_1 > var_2 > var_3 or var_2 > var_1 > var_3:
        print(var_1 + var_2)
    elif var_2 > var_3 > var_1 or var_3 > var_2 > var_1:
        print(var_2 + var_3)
    else:
        print(var_3 + var_1)


user_var1 = int(input('Введите число'))
user_var2 = int(input('Введите число'))
user_var3 = int(input('Введите число'))

summing(user_var1, user_var2, user_var3)
