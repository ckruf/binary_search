from typing import Sequence, Optional
import unittest
import math
import random

def binary_search(searchSpace: Sequence[int], target: int) -> bool:
    left = 0
    right = len(searchSpace) - 1 # subtracting 1 so we don't get index out of range errors
    iteration = 1 

    # <= is very important here, if it were <, then the search would fail to find a target found in the last position
    while (left <= right):
        mid = (left + ((right - left) / 2))
        # print(f"iteration {iteration} - left is: {left}, right is: {right}, mid is: {mid} ({math.ceil(mid)}), corresponding value: {searchSpace[math.ceil(mid)]}")

        # whether we put floor, ceil or round, the algorithm works
        mid = math.ceil(mid)
        if searchSpace[mid] == target:
            return True
        elif searchSpace[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        iteration += 1

    return False

binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1)

# Generates a sorted list of integers of specified length, containing a target number 
def generate_list_ints(length: int, target: Optional[int] = None)-> Sequence[int]:
    number_list = []
    if target:
        number_list.append(target)
    for _ in range(length):
        randomint = random.randrange(-500, 500)
        number_list.append(randomint)
    number_list.sort()
    return number_list

# binary_search([2, 3, 4, 5, 6, 7, 10, 11, 12, 14], 10)

class BinarySearchTests(unittest.TestCase):
    def test_even_length_success(self):
        self.assertTrue(binary_search([2, 3, 4, 5, 6, 7], 3))

    def test_even_length_last_success(self):
        self.assertTrue(binary_search([2, 3, 4, 5, 6, 7], 7))

    def test_even_length_first_success(self):
        self.assertTrue(binary_search([2, 3, 4, 5, 6, 7], 2))

    def test_even_length_failure(self):
        self.assertFalse(binary_search([2, 3, 4, 5, 6, 7], 8))

    def test_odd_length_success(self):
        self.assertTrue(binary_search([7, 10, 15, 16, 19, 24, 26], 10))

    def test_odd_length_first_success(self):
        self.assertTrue(binary_search([7, 10, 15, 16, 19, 24, 26], 7))

    def test_odd_length_last_success(self):
        self.assertTrue(binary_search([7, 10, 15, 16, 19, 24, 26], 26))

    def test_odd_length_failure(self):
        self.assertFalse(binary_search([7, 10, 15, 16, 19, 24, 26], 17))

    def test_random_list1(self):
        target = 30
        search_space = generate_list_ints(200, 30)
        self.assertTrue(binary_search(search_space, target))

    def test_random_list2(self):
        target = 17
        search_space = generate_list_ints(311, 17)
        self.assertTrue(binary_search(search_space, target))

    def test_random_list3(self):
        target = 189
        search_space = generate_list_ints(500, 189)
        self.assertTrue(binary_search(search_space, target))

    def test_random_list4(self):
        target = 200
        search_space = generate_list_ints(199)
        while 200 in search_space:
            search_space.remove(200)
        self.assertFalse(binary_search(search_space, 200))
        

if __name__ == '__main__':
    unittest.main()
