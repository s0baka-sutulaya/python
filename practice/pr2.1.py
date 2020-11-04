time = int(input('Введите время в секундах'))
hours = time // 3600
minute = time // 60 - hours*60
sec = time - hours*3600 - minute*60
print(hours, ":", minute, ":", sec)
