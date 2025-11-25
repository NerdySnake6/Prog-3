"""
Модуль для построения бинарного дерева в виде словаря.
"""

from typing import Callable, Optional


def gen_bin_tree(
    height: int = 4,
    root: int = 3,
    left_leaf: Optional[Callable[[int], int]] = None,
    right_leaf: Optional[Callable[[int], int]] = None
) -> Optional[dict]:
    """
    Рекурсивно строит бинарное дерево в виде словаря.

    Args:
        height: Высота дерева. При height=0 возвращает None.
        root: Значение корневого узла.
        left_leaf: Функция для вычисления левого потомка. По умолчанию root + 2.
        right_leaf: Функция для вычисления правого потомка. По умолчанию root * 3.

    Returns:
        Словарь с ключами 'root', 'left', 'right' или None если height <= 0.

    Raises:
        ValueError: Если height < 0.
    """
    if height < 0:
        raise ValueError("Height cannot be negative")
    if height == 0:
        return None
    
    # Устанавливаем функции по умолчанию
    if left_leaf is None:
        left_leaf = lambda x: x + 2
    if right_leaf is None:
        right_leaf = lambda x: x * 3
    
    return {
        'root': root,
        'left': gen_bin_tree(height - 1, left_leaf(root), left_leaf, right_leaf),
        'right': gen_bin_tree(height - 1, right_leaf(root), left_leaf, right_leaf)
    }


if __name__ == "__main__":
    # Демонстрация работы
    print("Демонстрация работы:")
    print("Дерево по умолчанию:", gen_bin_tree())
    print("Дерево height=2, root=5:", gen_bin_tree(2, 5))
    print("Дерево height=1, root=10:", gen_bin_tree(1, 10))
    
    # Демонстрация с пользовательскими функциями
    custom_tree = gen_bin_tree(
        height=2,
        root=1,
        left_leaf=lambda x: x * 2,
        right_leaf=lambda x: x + 3
    )
    print("Дерево с кастомными функциями:", custom_tree)