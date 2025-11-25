import unittest
from lab_4_bin_tree import gen_bin_tree


class TestBinaryTree(unittest.TestCase):
    
    def test_default_tree(self):
        tree = gen_bin_tree()
        # Для height=4 по умолчанию должно быть 4 уровня
        expected = {
            'value': 3,
            'left': {
                'value': 5,
                'left': {
                    'value': 7,
                    'left': {'value': 9},
                    'right': {'value': 21}
                },
                'right': {
                    'value': 15,
                    'left': {'value': 17},
                    'right': {'value': 45}
                }
            },
            'right': {
                'value': 9,
                'left': {
                    'value': 11,
                    'left': {'value': 13},
                    'right': {'value': 33}
                },
                'right': {
                    'value': 27,
                    'left': {'value': 29},
                    'right': {'value': 81}
                }
            }
        }
        self.assertEqual(tree, expected)
    
    def test_small_tree(self):
        tree = gen_bin_tree(height=2, root=5)
        expected = {
            'value': 5,
            'left': {'value': 7},
            'right': {'value': 15}
        }
        self.assertEqual(tree, expected)
    
    def test_only_root(self):
        tree = gen_bin_tree(height=1, root=10)
        expected = {'value': 10}
        self.assertEqual(tree, expected)
    
    def test_empty_tree(self):
        tree = gen_bin_tree(height=0, root=10)
        expected = {'value': 10}
        self.assertEqual(tree, expected)
    
    def test_custom_functions(self):
        tree = gen_bin_tree(
            height=2,
            root=1,
            left_branch=lambda x: x * 2,
            right_branch=lambda x: x + 3
        )
        expected = {
            'value': 1,
            'left': {'value': 2},
            'right': {'value': 4}
        }
        self.assertEqual(tree, expected)


if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)