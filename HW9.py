import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def dollar_exchange_rate():
    url = "НЕПОДСОЕДИНЯЕТЬСЯ НЕ ЗНАЮ ЧОМУ"
    response = requests.get(url)
    data = response.json()

    if "rates" in data and "SEK" in data["rates"]:
        return data["rates"]["SEK"]
    else:
        raise ValueError("Не вдалося отримати курс долара!")

try:
    today = datetime.now().strftime("%Y-%m-%d")
    rate = dollar_exchange_rate()
    logging.info(f"Курс долара на {today}: 1 USD = {rate:.2f} SEK")

    amount_sek = float(input("Введіть суму в SEK: "))
    amount_usd = amount_sek / rate
    print(f"{amount_sek:.2f} SEK = {amount_usd:.2f} USD")

except Exception as e:
    logging.error(f"Сталася помилка: {e}")