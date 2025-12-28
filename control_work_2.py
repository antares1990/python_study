import pandas as pd
import re
from typing import List, Optional

#1. Класс Employee
class Employee:
    def __init__(self, name: str, position: str, salary: float, hours_worked: int = 0):
        self.name = name
        self.position = position
        self.salary = salary
        self.hours_worked = hours_worked

    #добавляет отработанные часы
    def add_hours(self, hours: int) -> None:
        if hours < 0:
            raise ValueError("Количество часов не может быть отрицательным")
        self.hours_worked += hours

    #возвращает зарплату на основе отработанных часов, считая ставку как месячную зарплату, делённую на 160 часов
    def calculate_pay(self) -> float:
        salary = self.salary / 160
        return salary * self.hours_worked

#2. Класс Task
class Task:
    def __init__(self, title: str, description: str = "", status: str = "В процессе"):
        self.title = title
        self.description = description
        self.status = status
        self.assigned_employee: Optional['Employee'] = None

    #назначает задачу сотруднику
    def assign_employee(self, employee: 'Employee') -> None:
        if not isinstance(employee, Employee):
            raise TypeError("Сотрудник не определен")
        self.assigned_employee = employee
        print(f"Задача '{self.title}' назначена сотруднику {employee.name}")

    #отмечает задачу как завершённую
    def mark_complete(self) -> None:
        if self.status == "Завершено":
            print(f"Задача '{self.title}' уже завершена")
            return
        self.status = "Завершено"
        print(f"Задача '{self.title}' отмечена как завершённая")

#3. Класс Project
class Project:
    def __init__(self, title: str):
        self.title = title
        self.tasks: List['Task'] = []

    #добавляет задачу к проекту
    def add_task(self, task: 'Task') -> None:
        if not isinstance(task, Task):
            raise TypeError("Можно добавлять только объекты класса Task")

        self.tasks.append(task)
        print(f"Задача '{task.title}' добавлена в проект '{self.title}'")

    #возвращает процент завершения проекта на основе статуса задач
    def project_progress(self) -> float:
        if not self.tasks:
            return 0.0
        completed_tasks = sum(1 for task in self.tasks if task.status == "Завершено")
        progress = (completed_tasks / len(self.tasks)) * 100
        return round(progress, 2)

#Проверка
if __name__ == "__main__":
    # Создаем сотрудников
    developer = Employee("Иван Иванов", "Разработчик", 40)
    # Создаем задачи
    task1 = Task("Разработка1", "Создание БД")
    task2 = Task("Разработка2", "Создание дизайна")
    task3 = Task("Разработка3", "Создание бэка")
    # Назначаем задачи сотруднику
    task1.assign_employee(developer)
    task2.assign_employee(developer)
    task3.assign_employee(developer)
    # Создаем проект
    project = Project("Разработка")
    # Добавляем задачи в проект
    project.add_task(task1)
    project.add_task(task2)
    project.add_task(task3)
    #Процент завершения задач:
    print(f"   Прогресс: {project.project_progress()}%")
    #Отмечаем задачи как завершенные
    task1.mark_complete()
    #Процент завершения задач:
    print(f"   Прогресс, если завершена 1 задача: {project.project_progress()}%")

print()

# Функции для работы с данными
# extract_emails(text) — находит все email-адреса в строке. Поиск нужно реализовать через регулярные выражения.
def extract_emails(text: str) -> List[str]:
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Ищем все совпадения в тексте
    emails = re.findall(pattern, text, re.IGNORECASE)
    return emails

#Проверка
if __name__ == "__main__":
    # Тестовые строки с email-адресами
    test_texts = (
        "Свяжитесь с нами по email: info@company.com или support@company.org " +
        "Мои контакты: user.name@gmail.com, test-user@mail.ru, contact123@yahoo.com "+
        "Неверные email: user@.com, @domain.com, user@domain. " +
        "Сложные email: john.doe@sub.domain.co.uk, user_name+tag@domain.com " +
        "Email в тексте: Пишите на contact@example.com. Также можно на admin@test.ru. " +
        "Несколько email в одной строке: a@b.c, test@example.com, hello@world.org " +
        "Email с цифрами: user123@domain45.com " +
        "Смешанный текст: Телефон: +7-999-123-45-67, email: contact@site.ru, адрес: г. Москва"
    )
    print(extract_emails(test_texts))

print()

#  read_csv_to_df(file_path)  — работает с pd.DataFrame: читает CSV-файл и удаляет строки с пропущенными значениями.
def read_csv_to_df(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)
    df_cleaned = df.dropna()
    return df_cleaned

# Проверка
# Пример использования
if __name__ == "__main__":
    # Создаем тестовый CSV-файл
    test_data = {
         'id': [1, 2, 3, 4, 5],
         'name': ['Alice', 'Bob', None, 'David', 'Eva'],
         'age': [25, 30, 35, None, 28],
         'email': ['alice@test.com', None, 'charlie@test.com', 'david@test.com', 'eva@test.com'],
         'salary': [50000, 60000, 55000, 70000, None]
     }

    test_df = pd.DataFrame(test_data)

    file_path = r'D:\test_data.csv'

    # Сохраняем тестовый файл
    test_df.to_csv(file_path, index=False, encoding='utf-8')
    # Читаем его
    df = read_csv_to_df(file_path)
    print(df)