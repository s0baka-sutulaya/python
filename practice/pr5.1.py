gain = int(input('Введите сумму выручки'))
charge = int(input('Введите сумму издержек'))
if gain > charge:
    print("Вы работаете с прибылью)")
    profit = gain - charge
    print('Рентабельность выручки = ', profit/gain)
    workers = int(input('Введите количество сотрудников'))
    print('Прибыль фирмы в расчете на 1 сотрудника = ', profit/workers)
elif gain < charge:
    print("Вы работаете с убытком(")
elif gain == charge:
    print("Вы работаете в 0(")
