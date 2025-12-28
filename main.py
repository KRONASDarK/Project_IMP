from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import requests as req

if __name__ == '__main__':
    current_date_and_time = datetime.now()
    formatted_date = current_date_and_time.strftime("%d.%m.%Y %H:%M:%S")
    print(f"Дата и время вывода: {formatted_date}")

    get_employees(5, 5)
    calculate_salary(5, 5)

    # Мини программа requests
    response = req.get('https://ya.ru/')

    if response.status_code == 200:
        print("Успешный get запрос ya.ru/")
        print(response.text)
    else:
        print(f"Ошибка: {response.status_code}")