# Задание No1.
# Постройте график отражающий время ходьбы в минутах и количество потраченных калорий. Воспользуйтесь приведенными ниже
# списками для минут и калорий соответственно. Не забудьте про заголовок графика, а также подписи к каждой из осей.
# Данные:
# minutes = [26, 42, 82]
# calories = [138, 229, 445]

import matplotlib.pyplot as plt

# Данные
minutes = [26, 42, 82]
calories = [138, 229, 445]

# Создаем график
plt.figure(figsize=(10, 6))
plt.plot(minutes, calories, marker='o', linestyle='-', color='red', linewidth=2, markersize=8)

# Настройки графика
plt.title('Зависимость потраченных калорий от времени ходьбы', fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Время ходьбы (минуты)', fontsize=12)
plt.ylabel('Потраченные калории', fontsize=12)

plt.tight_layout()
plt.show()


# Задача No2: Обновление цен на машины с учетом утильсбора
# У вас есть список машин и их цены. После введения утильсбора цена каждой машины увеличивается на 5%. Ваша задача - с
# помощью NumPy создать новый массив с обновлёнными ценами и наглядно показать, как изменились цены с помощью графиков.
# Данные:
# cars = ['A1', 'A8', 'A3', 'A4', 'A5', 'A6']
# prices = [1500000, 2500000, 1400000, 2200000, 1300000, 1450000]
# Алгоритм:
# 1. Преобразуйте список prices в массив NumPy.
# 2. Создайте новый массив с ценами после повышения на 5%.
# 3. Постройте два столбца для каждой машины:
# Первый — исходная цена.
# Второй — цена с утильсбором.
# 4. Добавьте:
# Подписи осей: "Цена", "₽", "Машины".
# Заголовок: "Влияние утильсбора на цены машин".
# Легенду: "Оригинальная цена", "С утильсбором".


import numpy as np
import matplotlib.pyplot as plt

# Данные
cars = ['A1', 'A8', 'A3', 'A4', 'A5', 'A6']
prices = [1500000, 2500000, 1400000, 2200000, 1300000, 1450000]

# Преобразование списка prices в массив NumPy
prices_np = np.array(prices)

# После повышения на 5%
prices_up = prices_np * 1.05

print("Исходные цены:", prices_np)
print("Цены с утильсбором:", prices_up)

# Построение графика
fig, ax = plt.subplots(figsize=(12, 6))

# Позиции для столбцов
x = np.arange(len(cars))
width = 0.20

# Создаем столбцы
bars1 = ax.bar(x - width/2, prices_np, width, label='Оригинальная цена', color='blue', alpha=0.8)
bars2 = ax.bar(x + width/2, prices_up, width, label='С утильсбором', color='orange', alpha=0.8)

# Настройки графика
ax.set_xlabel('Машины', fontsize=12)
ax.set_ylabel('Цена, ₽', fontsize=12)
ax.set_title('Изменение цены машины после введения утильсбора', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(cars)
ax.legend()

# Форматирование цен на оси Y (в миллионах)
def format_price(x, pos):
    return f'{x/1000000:.1f}M'

ax.yaxis.set_major_formatter(plt.FuncFormatter(format_price))

# Добавляем подписи значений на столбцах
def add_value_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height/1000000:.1f}M',
                ha='center', va='bottom', fontsize=9)

add_value_labels(bars1)
add_value_labels(bars2)

plt.tight_layout()
plt.show()