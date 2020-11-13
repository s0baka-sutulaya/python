result = 0
while True:
    numbers = input('Введите числа или q для выхода').split()
    for n in numbers:
        if n == 'q':
            print(result)
            break
        else:
            result += int(n)
            continue
    print(result)
