#!/usr/bin/python3

import unittest
import bubble
import selection
import insertion


class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.arr = [23, 1, 3, 4, 6, 18, 0, -1, 23.4, 2]
        self.sorted = sorted(self.arr)

    def test_sort_empty(self):
        arr = []
        bubble.sort(arr)
        self.assertEqual(arr, [])

    def test_sort_one(self):
        arr = ['a']
        bubble.sort(arr)
        self.assertEqual(arr, ['a'])

    def test_sort_two(self):
        arr = ['b', 'a']
        bubble.sort(arr)
        self.assertEqual(arr, ['a', 'b'])
        arr = ['c', 'd']
        self.assertEqual(arr, ['c', 'd'])

    def test_sort_mult(self):
        bubble.sort(self.arr)
        self.assertEqual(self.arr, self.sorted)

    def test_dup_values(self):
        arr = [1, 1, 1, 2, 2, 3, 1]
        bubble.sort(arr)
        self.assertEqual(arr, [1, 1, 1, 1, 2, 2, 3])


class TestSelectionSort(unittest.TestCase):

    def setUp(self):
        self.arr = [23, 1, 3, 4, 6, 18, 0, -1, 23.4, 2]
        self.sorted = sorted(self.arr)

    def test_sort_empty(self):
        arr = []
        selection.sort(arr)
        self.assertEqual(arr, [])

    def test_sort_one(self):
        arr = ['a']
        selection.sort(arr)
        self.assertEqual(arr, ['a'])

    def test_sort_two(self):
        arr = ['b', 'a']
        selection.sort(arr)
        self.assertEqual(arr, ['a', 'b'])
        arr = ['c', 'd']
        self.assertEqual(arr, ['c', 'd'])

    def test_sort_mult(self):
        selection.sort(self.arr)
        self.assertEqual(self.arr, self.sorted)

    def test_dup_values(self):
        arr = [1, 1, 1, 2, 2, 3, 1]
        selection.sort(arr)
        self.assertEqual(arr, [1, 1, 1, 1, 2, 2, 3])


class TestInsertionSort(unittest.TestCase):

    def setUp(self):
        self.arr = [23, 1, 3, 4, 6, 18, 0, -1, 23.4, 2]
        self.sorted = sorted(self.arr)

    def test_sort_empty(self):
        arr = []
        insertion.sort(arr)
        self.assertEqual(arr, [])

    def test_sort_one(self):
        arr = ['a']
        insertion.sort(arr)
        self.assertEqual(arr, ['a'])

    def test_sort_two(self):
        arr = ['b', 'a']
        insertion.sort(arr)
        self.assertEqual(arr, ['a', 'b'])
        arr = ['c', 'd']
        self.assertEqual(arr, ['c', 'd'])

    def test_sort_mult(self):
        insertion.sort(self.arr)
        self.assertEqual(self.arr, self.sorted)

    def test_dup_values(self):
        arr = [1, 1, 1, 2, 2, 3, 1]
        insertion.sort(arr)
        self.assertEqual(arr, [1, 1, 1, 1, 2, 2, 3])



if __name__ == "__main__":
    unittest.main()
