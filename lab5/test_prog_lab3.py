import unittest
from prog_lab3 import fact_recursive, fact_recursive_cached, fact_iterative, fact_iterative_cached

class TestFactorial(unittest.TestCase):

    def test_fact_recursive(self):
        self.assertEqual(fact_recursive(0), 1)
        self.assertEqual(fact_recursive(1), 1)
        self.assertEqual(fact_recursive(5), 120)

    def test_fact_recursive_cached(self):
        fact_recursive_cached.cache_clear()
        self.assertEqual(fact_recursive_cached(0), 1)
        self.assertEqual(fact_recursive_cached(1), 1)
        self.assertEqual(fact_recursive_cached(5), 120)

    def test_fact_iterative(self):
        self.assertEqual(fact_iterative(0), 1)
        self.assertEqual(fact_iterative(1), 1)
        self.assertEqual(fact_iterative(5), 120)

    def test_fact_iterative_cached(self):
        fact_iterative_cached.cache_clear()
        self.assertEqual(fact_iterative_cached(0), 1)
        self.assertEqual(fact_iterative_cached(1), 1)
        self.assertEqual(fact_iterative_cached(5), 120)

    def test_all_same_results(self):
        self.assertEqual(fact_recursive(10), fact_recursive_cached(10))
        self.assertEqual(fact_recursive(10), fact_iterative(10))
        self.assertEqual(fact_recursive(10), fact_iterative_cached(10))

if __name__ == '__main__':
    unittest.main()