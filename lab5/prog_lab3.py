import timeit
import matplotlib.pyplot as plt
from functools import lru_cache


def fact_recursive(n: int) -> int:
    """Рекурсивный факториал без мемоизации"""
    if n == 0:
        return 1
    return n * fact_recursive(n - 1)


@lru_cache(maxsize=None)
def fact_recursive_cached(n: int) -> int:
    """Рекурсивный факториал с мемоизацией"""
    if n == 0:
        return 1
    return n * fact_recursive_cached(n - 1)


def fact_iterative(n: int) -> int:
    """Нерекурсивный факториал"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


@lru_cache(maxsize=None)
def fact_iterative_cached(n: int) -> int:
    """Нерекурсивный факториал с мемоизацией"""
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def benchmark(func, n, number=1000, repeat=3):
    """Возвращает минимальное время выполнения func(n)"""
    times = timeit.repeat(lambda: func(n), number=number, repeat=repeat)
    return min(times)


def main():
    # фиксированный набор данных
    test_data = list(range(10, 100, 10))
    
    res_recursive = []
    res_recursive_cached = []
    res_iterative = []
    res_iterative_cached = []

    for n in test_data:
        print(f"Тестируем n={n}...")
        
        # Очищаем кэш перед каждым тестом для чистоты эксперимента
        fact_recursive_cached.cache_clear()
        fact_iterative_cached.cache_clear()
        
        res_recursive.append(benchmark(fact_recursive, n, number=1000, repeat=3))
        res_recursive_cached.append(benchmark(fact_recursive_cached, n, number=1000, repeat=3))
        res_iterative.append(benchmark(fact_iterative, n, number=1000, repeat=3))
        res_iterative_cached.append(benchmark(fact_iterative_cached, n, number=1000, repeat=3))

    # Визуализация
    plt.figure(figsize=(12, 6))
    plt.plot(test_data, res_recursive, 'ro-', label="Рекурсивный (без кэша)")
    plt.plot(test_data, res_recursive_cached, 'go-', label="Рекурсивный (с кэшем)")
    plt.plot(test_data, res_iterative, 'bo-', label="Итеративный (без кэша)")
    plt.plot(test_data, res_iterative_cached, 'mo-', label="Итеративный (с кэшем)")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.title("Сравнение методов вычисления факториала с мемоизацией")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Вывод результатов
    print("\nСравнение производительности:")
    print("n\tРекурсив\tРекурсив(кэш)\tИтератив\tИтератив(кэш)")
    print("-" * 70)
    for i, n in enumerate(test_data):
        print(f"{n}\t{res_recursive[i]:.6f}\t{res_recursive_cached[i]:.6f}\t{res_iterative[i]:.6f}\t{res_iterative_cached[i]:.6f}")


if __name__ == "__main__":
    main()