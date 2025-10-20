import unittest
from lab_4_bin_tree import gen_bin_tree

class TestBinaryTree(unittest.TestCase):
    
    def test_default_tree(self):
        tree = gen_bin_tree()
        self.assertEqual(tree['value'], 3)
        self.assertEqual(tree['left']['value'], 5)
        self.assertEqual(tree['right']['value'], 9)
    
    def test_small_tree(self):
        tree = gen_bin_tree(height=2, root=5)
        self.assertEqual(tree['value'], 5)
        self.assertEqual(tree['left']['value'], 7)
        self.assertEqual(tree['right']['value'], 15)
    
    def test_only_root(self):
        tree = gen_bin_tree(height=1, root=10)
        self.assertEqual(tree, {'value': 10})
    
    def test_empty_tree(self):
        tree = gen_bin_tree(height=0)
        self.assertEqual(tree, {})

if __name__ == '__main__':
    unittest.main()