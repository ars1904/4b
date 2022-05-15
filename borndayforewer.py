"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

def year_Pushkin():
    year = input('Ввведите год рождения А.С.Пушкина:')
    while year != '1799':
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина:')
    return year

def month_Pushkin():
    month = input('Ввведите месяц рождения Пушкин?')
    while month != '6':
        print("Не верно")
        month = input('В какой месяц родился Пушкин?')
    print('Верно')
    return month

def day_Pushkin():
    day = input('Ввведите день рождения Пушкин?')
    while day != '6':
        print("Не верно")
        day = input('В какой день июня родился Пушкин?')
    print('Верно')
    return day

def Pushkin():
    year=year_Pushkin()
    month=month_Pushkin()
    day=day_Pushkin()
    return print(f"Дата рождения Пушкина: {day}.{month}.{year}")

Pushkin()
