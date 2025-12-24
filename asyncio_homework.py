# Задача 1: "Базовая корутина"

import asyncio

async def main():
    print("Асинхронность - это просто!")

# Запуск асинхронной программы
asyncio.run(main())

print()

# Задача 2: "Цепочка событий"

import asyncio

async def prepare():
    await asyncio.sleep(0.1)
    print("Подготовка...")

async def execute():
    await asyncio.sleep(0.2)
    print("Выполнение...")

async def cleanup():
    await asyncio.sleep(0.05)
    print("Завершение...")

async def main():
    await prepare()
    await execute()
    await cleanup()

asyncio.run(main())