import logging
from datetime import datetime

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


#1
def log_info_date():
    today = datetime.now().strftime("%Y-%m-%d")
    logging.info(f"Поточна дата: {today}")
    print(f"[INFO] Поточна дата: {today}")


#2
def error_handling_example():
    try:
        x = 1 / 0  # Поділ на нуль
    except Exception as e:
        logging.error(f"Виникла помилка: {e}")
        print(f"[ERROR] Виникла помилка: {e}")


#3
def login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    try:
        assert username == correct_username and password == correct_password, \
            "Невірний пароль або ім'я користувача."
        print("Вхід виконано успішно")
    except AssertionError as e:
        print(e)


#4
def check_age(age):
    try:
        assert age >= 18, "Вам має бути 18 років або більше"
        print("Ви маєте право на використання цього сервіса.")
    except AssertionError as e:
        print(e)


#5
def process_list(input_list):
    try:
        assert len(input_list) >= 3, "Список повинен містити як мімімум 3 елементи"
        print(f"Список містить {len(input_list)} елементів")
    except AssertionError as e:
        print(e)