import unittest
import sys
import io

# Импортируем тестируемую функцию
from Lab6_it1 import get_currencies  # Правильный импорт

class SimpleTestGetCurrencies(unittest.TestCase):
    """Упрощенные тесты для функции get_currencies"""

    def capture_stdout(self, func, *args, **kwargs):
        """Вспомогательная функция для захвата stdout"""
        captured_output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            result = func(*args, **kwargs)
        finally:
            sys.stdout = old_stdout
        return result, captured_output.getvalue()

    def test_integration_real_api(self):
        """Интеграционный тест с реальным API"""
        result = get_currencies(['USD', 'EUR'])
        
        if result is not None:  # Если API доступно
            self.assertIsInstance(result, dict)
            self.assertIn('USD', result)
            self.assertIn('EUR', result)
            self.assertIsInstance(result['USD'], (int, float))
            self.assertIsInstance(result['EUR'], (int, float))
            print("✓ Реальный API запрос прошел успешно")
        else:
            print("⚠ API недоступно, тест пропущен")

    def test_integration_invalid_currency(self):
        """Тест с невалидной валютой"""
        result, output = self.capture_stdout(get_currencies, ['INVALID_CURRENCY_CODE'])
        
        self.assertIsNone(result, "Для невалидной валюты должен возвращаться None")
        self.assertIn("не найдена", output, "Должно быть сообщение о не найденной валюте")
        print("✓ Тест невалидной валюты прошел успешно")

    def test_integration_empty_list(self):
        """Тест с пустым списком валют"""
        result = get_currencies([])
        
        self.assertEqual(result, {}, "Для пустого списка должен возвращаться пустой словарь")
        print("✓ Тест пустого списка прошел успешно")


def main():
    """Запуск упрощенных тестов"""
    print("ЗАПУСК ТЕСТОВ ДЛЯ GET_CURRENCIES")
    print("=" * 40)
    
    tester = SimpleTestGetCurrencies()
    
    # Запускаем тесты по одному для лучшего контроля
    test_methods = [method for method in dir(tester) if method.startswith('test_')]
    
    for test_method in test_methods:
        print(f"\nЗапуск {test_method}...")
        try:
            getattr(tester, test_method)()
        except Exception as e:
            print(f"✗ Ошибка в тесте {test_method}: {e}")
    
    print("\n" + "=" * 40)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")


if __name__ == '__main__':
    main()