def person(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


information = input('Введите через пробел имя, фамилию, год рождения, город, email, номер телефона')
user_inf = list(information.split())

person(name=user_inf[0], surname=user_inf[1], year=user_inf[2], city=user_inf[3], email=user_inf[4], phone=user_inf[5])
