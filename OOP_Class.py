# Задание №1.

print("Задание №1")
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def add(self, amount):
        if amount <= 0:
            return "Сумма для пополнения должна быть положительной"

        else:
            self.balance += amount
            return f"Счет пополнен на {amount:.2f}. Новый баланс: {self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Сумма для снятия должна быть положительной"

        if amount > self.balance:
            return f"Недостаточно средств на счете. Баланс счета: {self.balance:.2f}"

        else:
            self.balance -= amount
            return f"Со счета снято {amount:.2f}. Новый баланс: {self.balance:.2f}"

# Примеры использования:
if __name__ == "__main__":
    account = BankAccount("1", 10000)

    # Пополнение счета
    print(f"Пополнение счета на положительную сумму: {account.add(500)}")
    print(f"Пополнение счета на отрицательную сумму: {account.add(-100)}")

    # Снятие средств
    print(f"Снятие со счета корректной суммы: {account.withdraw(300)}")
    print(f"Снятие со счета большей суммы: {account.withdraw(20000)}")
    print(f"Снятие со счета отрицательной суммы: {account.withdraw(-50)}")


#Задание №2.

print("\nЗадание №2")
class Product:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

    def change_amount(self, change_amount):
        if abs(change_amount) > self.amount:
            return f"Товара '{self.name}' недостаточно на складе"

        else:
            self.amount += change_amount
            new_price = self.amount*self.price
            return f"Новое количество товара '{self.name}' - {self.amount}\nНовая стоимость товара '{self.name}' - {new_price}"

    def apply_discount(self, discount):
        if discount < 0 or discount > 100:
            print(f"Ошибка: Скидка должна быть в диапазоне от 0 до 100%")
            return self.price

        else:
            discount = self.price * (discount / 100)
            self.price -= discount
            return f"Старая цена - {self.price + discount:.2f}\nНовая цена - {self.price:.2f}"

# Примеры использования:
if __name__ == "__main__":
    table = Product("Стол", 10000, 10)

    # Изменение количества
    print(f"Увеличение количества товара: {table.change_amount(5)}")
    print(f"Уменьшение количества товара: {table.change_amount(-3)}")
    print(f"Уменьшение товара на превышающее количество: {table.change_amount(-20)}")

    # Применение скидки
    print(f"Применение корректной скидки: {table.apply_discount(15)}")
    print(f"Применение некорректной скидки: {table.apply_discount(120)}")

