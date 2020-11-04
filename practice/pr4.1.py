number = int(input('Введите целое положительное число'))
maximum = number % 10
number = number // 10
while number > 0:
    if maximum < number % 10:
        maximum = number % 10
    number = number // 10
print("Максимальное число = ", maximum)

