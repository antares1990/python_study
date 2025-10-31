# Задача No1. Магическая дата

def is_magic(date):
    date = date.replace(" ", "")
    day, month, year = map(int, date.split('.'))
    last_two_number = year % 100
    if day * month == last_two_number:
        return True
    else:
        return False

date = input("Ведите дату в формате dd.mm.yyyy ")
print(is_magic(date))


# Задача No2. Генератор лотерейных билетов

import random
tickets = set()

while len(tickets) != 100:
    random_number = random.randint(1000000, 9999999)
    tickets.add(random_number)

print(tickets)
print(len(tickets))


# Задача No3. Калькулятор доставки

def get_shipping_cost(quantity):
    cost = 1000 + (quantity - 1) * 120
    return cost

quantity = int(input("Введите количество товара = "))
print(get_shipping_cost(quantity))