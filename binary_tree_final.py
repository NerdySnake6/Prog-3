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
    import unittest
    
    class TestBinaryTree(unittest.TestCase):
        def test_default_params(self):
            tree = gen_bin_tree()
            self.assertIsNotNone(tree)
            self.assertEqual(tree['root'], 3)

        def test_custom_params(self):
            tree = gen_bin_tree(2, 5)
            expected = {
                'root': 5,
                'left': {'root': 7, 'left': None, 'right': None},
                'right': {'root': 15, 'left': None, 'right': None}
            }
            self.assertEqual(tree, expected)

        def test_zero_height(self):
            self.assertIsNone(gen_bin_tree(0, 5))

        def test_leaf_calculation(self):
            tree = gen_bin_tree(2, 10)
            self.assertEqual(tree['left']['root'], 12)  # 10 + 2
            self.assertEqual(tree['right']['root'], 30)  # 10 * 3

        def test_height_1(self):
            tree = gen_bin_tree(1, 10)
            self.assertEqual(tree['root'], 10)
            self.assertIsNone(tree['left'])
            self.assertIsNone(tree['right'])

    # Запуск демонстрации
    print("Демонстрация работы:")
    print("Дерево по умолчанию:", gen_bin_tree())
    print("Дерево height=2, root=5:", gen_bin_tree(2, 5))
    print("Дерево height=1, root=10:", gen_bin_tree(1, 10))
    
    # Запуск тестов
    print("\nЗапуск тестов...")
    unittest.main(argv=[''], exit=False, verbosity=2)