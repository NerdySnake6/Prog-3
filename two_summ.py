"""
Two Sum Solution
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    raise ValueError("No solution found")

# Тесты
import unittest

class TestTwoSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sorted(two_sum([2,7,11,15], 9)), [0,1])
    
    def test_example2(self):
        self.assertEqual(sorted(two_sum([3,2,4], 6)), [1,2])
    
    def test_example3(self):
        self.assertEqual(sorted(two_sum([3,3], 6)), [0,1])
    
    def test_no_solution(self):
        with self.assertRaises(ValueError):
            two_sum([1,2,3], 10)

if __name__ == "__main__":
    # Демонстрация работы
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6)
    ]
    
    for nums, target in test_cases:
        result = two_sum(nums, target)
        print(f"nums={nums}, target={target} -> {result}")
    
    # Запуск тестов
    print("\nЗапуск тестов...")
    unittest.main(argv=[''], verbosity=2, exit=False)