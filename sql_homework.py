
import tkinter as tk

from tkinter import ttk, messagebox

import psycopg2


import pandas as pd



# ===== Подключение к базе =====

conn = psycopg2.connect(

    host="localhost",

    database="te1",  # имя вашей базы

    user="postgres",

    password="1234",

    port=5432

)

cur = conn.cursor()



# ===== Главное окно =====

root = tk.Tk()

root.title("CRUD с PostgreSQL")

root.geometry("500x400")



# ===== Поля ввода =====

ttk.Label(root, text="Имя:").pack(pady=5)

name_entry = ttk.Entry(root)

name_entry.pack(fill="x", padx=10)



ttk.Label(root, text="Возраст:").pack(pady=5)

age_entry = ttk.Entry(root)

age_entry.pack(fill="x", padx=10)



# ===== Функции =====

def clear_fields():

    name_entry.delete(0, tk.END)

    age_entry.delete(0, tk.END)



def refresh_table():

    """Обновляем таблицу, загружая данные из базы"""

    for row in table.get_children():

        table.delete(row)

    cur.execute("SELECT * FROM users ORDER BY id")

    for row in cur.fetchall():

        table.insert("", "end", values=row)



def add_data():

    name = name_entry.get()

    age = age_entry.get()

    if name == "" or age == "":

        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля")

        return

    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))

    conn.commit()

    refresh_table()

    clear_fields()


def update_data():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Ошибка", "Выберите строку для обновления")
        return

    row_data = table.item(selected, "values")
    row_id = row_data[0]  # ID записи
    current_name = row_data[1]  # Текущее имя
    current_age = row_data[2]  # Текущий возраст

    new_name = name_entry.get()
    new_age = age_entry.get()

    if new_name == "" or new_age == "":
        messagebox.showwarning("Ошибка", "Пожалуйста, заполните все поля для обновления")
        return

    cur.execute("UPDATE users SET name = %s, age = %s WHERE id = %s",(new_name, new_age, row_id))
    conn.commit()

    refresh_table()
    clear_fields()


def delete_data():

    selected = table.focus()

    if not selected:

        messagebox.showwarning("Ошибка", "Выберите строку для удаления")

        return

    row_id = table.item(selected, "values")[0]

    cur.execute("DELETE FROM users WHERE id=%s", (row_id,))

    conn.commit()

    refresh_table()

    clear_fields()



def export_to_excel():

    """Выгрузка данных в Excel"""

    cur.execute("SELECT * FROM users ORDER BY id")

    rows = cur.fetchall()

    df = pd.DataFrame(rows, columns=["ID", "Имя", "Возраст"])

    df.to_excel("users.xlsx", index=False)

    messagebox.showinfo("Успех", "Данные успешно экспортированы в users.xlsx")


def five_old():
    # Очищаем таблицу
    for row in table.get_children():
        table.delete(row)

    cur.execute("""
            SELECT id, name, age 
            FROM users 
            ORDER BY age DESC 
            LIMIT 5
        """)

    top_users = cur.fetchall()

    # Вставляем данные в таблицу
    for row in top_users:
        table.insert("", "end", values=row)


# ===== Кнопки =====

tk.Button(root, text="Добавить", command=add_data, bg="lightgreen", fg="black").pack(fill="x", padx=10, pady=5)

tk.Button(root, text="Удалить", command=delete_data, bg="lightcoral", fg="black").pack(fill="x", padx=10, pady=5)

tk.Button(root, text="Обновить", command=update_data, bg="lightblue", fg="black").pack(fill="x", padx=10, pady=5)

tk.Button(root, text="Очистить поля", command=clear_fields).pack(fill="x", padx=10, pady=5)

tk.Button(root, text="Экспорт в Excel", command=export_to_excel).pack(fill="x", padx=10, pady=5)

tk.Button(root, text="ТОП-5 пожилых", command=five_old).pack(fill="x", padx=10, pady=5)



# ===== Таблица =====

table = ttk.Treeview(root, columns=("id", "name", "age"), show="headings")

table.heading("id", text="ID")

table.heading("name", text="Имя")

table.heading("age", text="Возраст")

table.pack(fill="both", expand=True, padx=10, pady=10)



# ===== Загрузка данных при старте =====

refresh_table()



# ===== Запуск окна =====

root.mainloop()
