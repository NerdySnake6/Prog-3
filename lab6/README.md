Лабораторная работа: Курсы валют ЦБ РФ
Установка
bash
pip install requests
Файлы проекта
Lab_it1.py - Базовая версия с логированием в stdout

Lab_it2.py - Логирование через декоратор

Lab_it3.py - Логирование через модуль logging

test_lab1.py, test_lab2.py, test_lab3.py - Тесты

test_all.py - Все тесты сразу

Использование
python
from Lab_it1 import get_currencies

# Получение курсов валют
rates = get_currencies(['USD', 'EUR', 'GBP'])
print(rates)  # {'USD': 81.35, 'EUR': 94.19, 'GBP': 106.96}
Описание итераций
Итерация 1 - Базовая реализация с обработкой ошибок в stdout

Итерация 2 - Логирование вынесено в декоратор log_errors_to_stdout

Итерация 3 - Профессиональное логирование через модуль logging

Запуск тестов
bash
# Тесты для конкретной итерации
python -m unittest test_lab1.py

# Все тесты
python test_all.py
API
URL: https://www.cbr-xml-daily.ru/daily_json.js

Функция возвращает словарь с курсами валют или None при ошибке.
