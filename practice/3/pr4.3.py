x = int(input('Введите положительное число'))
y = int(input('Введите отрицательное число'))

for n in range(abs(y)):
    x = x * x

print(1 / x)
