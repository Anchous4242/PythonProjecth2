#1
users = {
    "Егор": "дитина",
    "Тимофій": "підліток",
    "Софія": "дорослий",
    "Ксенія": "підліток",
    "Антон": "пенсіонер"
}

name = input("Введіть ім'я користувача: ")

if name in users:
    print(f"{name} належить до вікової групи: {users[name]}")
else:
    print(f"Користувача з іменем '{name}' не знайдено.")

#2

try:
    user_input = input("Введіть число: ")
    print("Ви ввели ціле число:", int(user_input))
except ValueError:
    print("Помилка: введене значення не можна перетворити на ціле число.")

#3
try:
    file_path = input("Введіть шлях до файлу: ")
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Вміст файлу:")
        print(content)
except FileNotFoundError:
    print("Помилка, файл не знайдено.")
except IOError:
    print("Помилка, не вдалося прочитати файл.")

#4
import math

function_names = ["sqrt", "not_exist"]

for name in function_names:
    try:
        func = getattr(math, name)
        result = func(16)
        print(f"Результат {name}(16): {result}")
    except AttributeError:
        print(f"Помилка: функцію '{name}' не знайдено в модулі 'math'.")
    except Exception as e:
        print(f"Інша помилка при виклику функції '{name}': {e}")