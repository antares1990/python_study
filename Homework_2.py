# Задача №1. Проверка надёжности пароля
# Напишите функцию `is_password_good(password)`, которая проверяет, является ли пароль надёжным

print("Задача №1")

def is_password_good(password):
        if (len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password)):
            return True
        else:
            return False

password = input("Введите пароль: ")

print(is_password_good(password))


# Задача №2. Программа для мини-банка
# Реализуйте программу, состоящую из трёх функций

print("\nЗадача №2")

from datetime import datetime
from zoneinfo import ZoneInfo

def greet_client(first_name, last_name):
    time = datetime.now(ZoneInfo('Europe/Moscow')).hour
    if time < 6:
        greet = "Доброй ночи"
    elif time < 12:
        greet = "Доброе утро"
    elif time < 18:
        greet = "Добрый день"
    else:
        greet = "Добрый вечер"
    return f"{greet}, {first_name} {last_name}"

def deposit(balance, amount):
    if amount > 0:
        return balance + amount
    else:
        return f"Ошибка: сумма пополнения должна быть положительной."

def withdraw(balance, amount):
    if amount > 0 and amount <= balance:
        return balance - amount
    elif amount <= 0:
        return f"Ошибка: сумма снятия должна быть положительной. Ваш баланс {balance}"
    else:
        return f"Ошибка: недостаточно средств на счёте. Ваш баланс {balance}"

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

print(greet_client(first_name, last_name))

balance = int(input("Введите баланс счета: "))
deposit_amount = int(input("Введите сумму пополнения: "))

print(deposit(balance, deposit_amount))

balance = int(input("Введите баланс счета: "))
withdraw_amount = int(input("Введите сумму снятия: "))

print(withdraw(balance, withdraw_amount))


# Задача №3 (ДОПОЛНИТЕЛЬНАЯ). Программа для мини-банка (версия со словарём)
# Дан словарь `clients`, где ключи — полные имена клиентов (`\"Имя Фамилия\"`), а значения — их балансы (целые числа).
# Реализуйте три функции, которые **принимают этот словарь** и **изменяют его напрямую

print("\nЗадача №3")

from datetime import datetime
from zoneinfo import ZoneInfo

def greet_client(clients, first_name, last_name):
    full_name = f"{first_name} {last_name}"
    if full_name in clients:
        time = datetime.now(ZoneInfo('Europe/Moscow')).hour
        if time < 6:
            greet = "Доброй ночи"
        elif time < 12:
            greet = "Доброе утро"
        elif time < 18:
            greet = "Добрый день"
        else:
            greet = "Добрый вечер"
        return f"{greet}, {first_name} {last_name}"
    else:
        return f"Клиента нет в словаре"

def deposit(clients, first_name, last_name, amount):
    full_name = f"{first_name} {last_name}"
    if greet_client(clients, first_name, last_name) == "Клиента нет в словаре":
        return f"Клиента нет в словаре"
    else:
        if amount > 0:
            clients[full_name] = clients[full_name] + amount
            return f"Счёт {full_name} пополнен. Новый баланс: {clients[full_name]}"
        else:
            return f"Ошибка: сумма пополнения должна быть положительной.Ваш баланс {clients[full_name]}"

def withdraw(clients, first_name, last_name, amount):
    full_name = f"{first_name} {last_name}"
    if greet_client(clients, first_name, last_name) == "Клиента нет в словаре":
        return f"Клиента нет в словаре"
    else:
        if amount > 0 and amount <= clients[full_name]:
            clients[full_name] = clients[full_name] - amount
            return f"Вывод: Со счёта {full_name} снято {amount}. Новый баланс: {clients[full_name]}"
        elif amount <= 0:
            return f"Ошибка: сумма снятия должна быть положительной. Ваш баланс {clients[full_name]}"
        else:
            return f"Ошибка: недостаточно средств на счёте. Ваш баланс {clients[full_name]}"

clients = {
    "Иван Иванов": 1500,
    "Мария Петрова": 2300,
    "Алексей Сидоров": 1800,
    "Елена Козлова": 3200,
    "Дмитрий Волков": 2750
}

first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")

print(greet_client(clients, first_name, last_name))

deposit_amount = int(input("Введите сумму пополнения: "))

print(deposit(clients, first_name, last_name, deposit_amount))

withdraw_amount = int(input("Введите сумму снятия: "))

print(withdraw(clients, first_name, last_name, withdraw_amount))

print(clients)

