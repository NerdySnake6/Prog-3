"""
Модуль для нерекурсивного построения бинарного дерева.
"""

from collections import deque



def gen_bin_tree(
    height: int = 4,
    root: int = 3,
    left_branch = lambda x: x + 2,
    right_branch = lambda x: x * 3
) -> dict:
    """
    Создает бинарное дерево без рекурсии.

    Args:
        height: Высота дерева. При height=0 возвращает словарь с корнем.
        root: Значение корневого узла.
        left_branch: Функция для вычисления левого потомка. По умолчанию root + 2.
        right_branch: Функция для вычисления правого потомка. По умолчанию root * 3.

    Returns:
        Словарь с ключами 'value', 'left', 'right'.
    """
    if height <= 0:
        return {'value': root}
    
    tree = {'value': root}
    
    if height == 1:
        return tree
    
    queue = deque([tree])
    
    while queue:
        current_node = queue.popleft()
        current_value = current_node['value']
        
        # Создаем левого потомка
        left_value = left_branch(current_value)
        current_node['left'] = {'value': left_value}
        queue.append(current_node['left'])
        
        # Создаем правого потомка  
        right_value = right_branch(current_value)
        current_node['right'] = {'value': right_value}
        queue.append(current_node['right'])
        
        # Проверяем глубину по количеству элементов в очереди
        # Максимальная глубина = 2^(height-1) - 1
        max_nodes_at_level = 2 ** (height - 1)
        if len(queue) >= max_nodes_at_level:
            break
    
    return tree


if __name__ == "__main__":
    # Создаем одно дерево с параметрами по умолчанию
    tree = gen_bin_tree()
    print(tree)