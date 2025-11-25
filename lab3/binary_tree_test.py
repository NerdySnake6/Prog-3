import unittest
from binary_tree import gen_bin_tree


class TestBinaryTree(unittest.TestCase):
    def test_default_params(self):
        """Тест с параметрами по умолчанию."""
        tree = gen_bin_tree()
        self.assertIsNotNone(tree)
        self.assertEqual(tree['root'], 3)

    def test_custom_params(self):
        """Тест с пользовательскими параметрами."""
        tree = gen_bin_tree(2, 5)
        expected = {
            'root': 5,
            'left': {
                'root': 7,
                'left': None,
                'right': None
            },
            'right': {
                'root': 15,
                'left': None,
                'right': None
            }
        }
        self.assertEqual(tree, expected)

    def test_zero_height(self):
        """Тест с высотой 0."""
        self.assertIsNone(gen_bin_tree(0, 5))

    def test_negative_height(self):
        """Тест с отрицательной высотой."""
        with self.assertRaises(ValueError):
            gen_bin_tree(-1, 5)

    def test_custom_functions(self):
        """Тест с пользовательскими функциями."""
        tree = gen_bin_tree(
            height=2,
            root=1,
            left_leaf=lambda x: x * 2,
            right_leaf=lambda x: x + 3
        )
        expected = {
            'root': 1,
            'left': {
                'root': 2,
                'left': None,
                'right': None
            },
            'right': {
                'root': 4,
                'left': None,
                'right': None
            }
        }
        self.assertEqual(tree, expected)

    def test_height_1(self):
        """Тест с высотой 1."""
        tree = gen_bin_tree(1, 10)
        expected = {
            'root': 10,
            'left': None,
            'right': None
        }
        self.assertEqual(tree, expected)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)