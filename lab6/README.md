Лабораторная работа: Получение курсов валют через API ЦБ РФ
Описание проекта
Проект состоит из трех итераций реализации функции get_currencies() для получения курсов валют через API Центрального Банка РФ с постепенным улучшением архитектуры и добавлением логирования.

Структура проекта
text
currency_api_project/
├── Lab_it1.py          # Итерация 1: Базовая реализация с логированием в stdout
├── Lab_it2.py          # Итерация 2: Логирование вынесено в декоратор
├── Lab_it3.py          # Итерация 3: Логирование через модуль logging
├── test_lab1.py        # Тесты для первой итерации
├── test_lab2.py        # Тесты для второй итерации
├── test_lab3.py        # Тесты для третьей итерации
├── test_all.py         # Общий тестовый файл для всех итераций
└── README.md           # Этот файл
Установка и настройка
Установка зависимостей
bash
pip install requests
Или для Python 3:

bash
pip3 install requests
Проверка установки
python
import requests
print("Requests установлен успешно!")
Описание итераций
Итерация 1: Базовая реализация (Lab_it1.py)
Особенности:

Прямое обращение к API ЦБ РФ

Логирование ошибок через sys.stdout

Обработка основных исключений

Использование:

python
from Lab_it1 import get_currencies

result = get_currencies(['USD', 'EUR', 'GBP'])
print(result)  # {'USD': 81.3562, 'EUR': 94.1954, 'GBP': 106.9671}
Итерация 2: Логирование через декоратор (Lab_it2.py)
Особенности:

Логирование вынесено в декоратор log_errors_to_stdout

Более чистая архитектура кода

Разделение бизнес-логики и обработки ошибок

Использование:

python
from Lab_it2 import get_currencies

result = get_currencies(['USD', 'EUR'])
Итерация 3: Логирование через модуль logging (Lab_it3.py)
Особенности:

Использование стандартного модуля logging

Запись логов как в консоль, так и в файл currency_rates.log

Гибкая настройка уровня логирования

Использование:

python
from Lab_it3 import get_currencies, setup_logging

setup_logging()  # Настройка логирования
result = get_currencies(['USD', 'EUR'])
API ЦБ РФ
URL по умолчанию: https://www.cbr-xml-daily.ru/daily_json.js

Пример ответа API:

json
{
  "Date": "2025-11-12T11:30:00+03:00",
  "Valute": {
    "USD": {
      "ID": "R01235",
      "NumCode": "840",
      "CharCode": "USD", 
      "Nominal": 1,
      "Name": "Доллар США",
      "Value": 81.3562,
      "Previous": 81.0132
    }
  }
}
Примеры использования
Базовый пример
python
from Lab_it1 import get_currencies

currencies = get_currencies(['USD', 'EUR', 'CNY', 'JPY'])
if currencies:
    for code, rate in currencies.items():
        print(f"{code}: {rate} руб.")
Пример с обработкой ошибок
python
from Lab_it1 import get_currencies

# Запрос несуществующей валюты
result = get_currencies(['INVALID_CODE'])
if result is None:
    print("Валюта не найдена")

# Запрос к неверному URL
result = get_currencies(['USD'], 'https://invalid-url.com')
if result is None:
    print("Ошибка подключения к API")
Полный рабочий пример
python
from Lab_it1 import get_currencies

def main():
    print("=== КОНВЕРТЕР ВАЛЮТ ===")
    
    # Список доступных валют
    available_currencies = ['USD', 'EUR', 'GBP', 'CNY', 'JPY', 'KZT']
    print(f"Доступные валюты: {', '.join(available_currencies)}")
    
    # Запрос валют у пользователя
    selected = input("Введите коды валют через запятую: ").upper().split(',')
    selected = [code.strip() for code in selected if code.strip()]
    
    # Получение курсов
    rates = get_currencies(selected)
    
    if rates:
        print("\nТЕКУЩИЕ КУРСЫ ЦБ РФ:")
        for currency, rate in rates.items():
            print(f"{currency}: {rate:.2f} руб.")
    else:
        print("Не удалось получить данные о курсах валют")

if __name__ == "__main__":
    main()
Тестирование
Запуск тестов для конкретной итерации
bash
# Тесты для первой итерации
python -m unittest test_lab1.py

# Тесты для второй итерации  
python -m unittest test_lab2.py

# Тесты для третьей итерации
python -m unittest test_lab3.py
Запуск всех тестов
bash
python test_all.py
Интеграционное тестирование
python
from Lab_it1 import get_currencies

# Тест реального API
result = get_currencies(['USD', 'EUR'])
if result:
    print("API работает корректно")
    print(f"USD: {result['USD']}, EUR: {result['EUR']}")
else:
    print("API недоступно")
Обработка ошибок
Функция обрабатывает следующие типы ошибок:

Ошибки сети - проблемы с подключением к API

Неверный формат данных - отсутствие ключа 'Valute' в ответе

Несуществующие валюты - запрос кодов, которых нет в API

HTTP ошибки - коды ответа 4xx/5xx

Доступные коды валют
Основные популярные валюты:

USD - Доллар США

EUR - Евро

GBP - Фунт стерлингов

CNY - Китайский юань

JPY - Японская иена

KZT - Казахстанский тенге

TRY - Турецкая лира

CHF - Швейцарский франк

Полный список доступен в ответе API по адресу: https://www.cbr-xml-daily.ru/daily_json.js

Особенности реализации
Итерация 1
Простая и понятная реализация

Прямая обработка исключений в функции

Вывод ошибок в стандартный поток вывода

Итерация 2
Разделение ответственности через декоратор

Упрощение основной функции

Возможность повторного использования декоратора

Итерация 3
Профессиональное логирование через стандартный модуль

Запись логов в файл для последующего анализа

Гибкая настройка уровней логирования
