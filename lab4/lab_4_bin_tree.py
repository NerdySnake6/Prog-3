from collections import deque

def gen_bin_tree(height=4, root=3, left_branch=None, right_branch=None):
    """
    Создает бинарное дерево без рекурсии
    """
    if left_branch is None:
        left_branch = lambda x: x + 2
    if right_branch is None:
        right_branch = lambda x: x * 3
    
    if height <= 0:
        return {}
    
    tree = {'value': root}
    
    if height == 1:
        return tree
    
    queue = deque()
    queue.append((tree, 1))
    
    while queue:
        current_node, level = queue.popleft()
        
        if level >= height:
            continue
        
        current_value = current_node['value']
        
        # Левый потомок
        left_value = left_branch(current_value)
        current_node['left'] = {'value': left_value}
        queue.append((current_node['left'], level + 1))
        
        # Правый потомок  
        right_value = right_branch(current_value)
        current_node['right'] = {'value': right_value}
        queue.append((current_node['right'], level + 1))
    
    return tree

# Создаем одно дерево с параметрами по умолчанию
tree = gen_bin_tree()
print(tree)