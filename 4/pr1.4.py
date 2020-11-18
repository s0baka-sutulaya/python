def calc(hours, payment, reward):
    hours = input('Введите количество часов работы')
    payment = input('Введите оплату за час')
    reward = input('Введите сумму премии')
    return (hours * payment) + reward
