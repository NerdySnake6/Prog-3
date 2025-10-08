"""Построение бинарного дерева в виде словаря."""

def gen_bin_tree(height=4, root=3):
    """
    Строит бинарное дерево рекурсивно.
    
    Левый потомок: root + 2, правый потомок: root * 3.
    """
    if height == 0:
        return None

    return {
        'root': root,
        'left': gen_bin_tree(height - 1, root + 2),
        'right': gen_bin_tree(height - 1, root * 3)
    }


if __name__ == "__main__":
    # Демонстрация работы
    print("Демонстрация работы:")
    print("Дерево по умолчанию:", gen_bin_tree())
    print("Дерево height=2, root=5:", gen_bin_tree(2, 5))
    print("Дерево height=1, root=10:", gen_bin_tree(1, 10))
