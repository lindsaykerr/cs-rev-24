#!/usr/bin/python3

import unittest
import stack


class TestStack(unittest.TestCase):

    def setUp(self):

        self.stack = stack.Stack()

    def test_add_stack(self):

        self.assertEqual(self.stack.size(), 0)
        self.stack.push(3)
        self.assertEqual(self.stack.size(), 1)
        self.stack.push(10)
        self.assertEqual(self.stack.size(), 2)

    def test_remove_from_stack(self):

        self.assertEqual(self.stack.size(), 0)
        with self.assertRaises(IndexError):
            self.stack.pop()

        self.stack.push(3)
        self.stack.push(4)
        self.stack.push(5)
        self.assertEqual(self.stack.size(), 3)
        self.assertEqual(self.stack.pop(), 5)
        self.assertEqual(self.stack.pop(), 4)
        self.assertEqual(self.stack.pop(), 3)

        self.assertEqual(self.stack.size(), 0)

    def test_peek(self):

        self.assertEqual(self.stack.peek(), None)
        self.stack.push(23)
        self.assertEqual(self.stack.peek(), 23)
        self.stack.push(43)
        self.stack.push(33)
        self.assertEqual(self.stack.peek(), 33)
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertEqual(self.stack.peek(), None)

    def test_stack_is_empty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(3)
        self.assertFalse(self.stack.isEmpty())
        self.stack.pop()
        self.assertTrue(self.stack.isEmpty())


if __name__ == '__main__':
    unittest.main()
