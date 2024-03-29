#!/usr/bin/python3

import unittest
import stack
from queue import Queue
from dequeue import Dequeue
from linked_list import LinkedList


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


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_add_items_to_queue(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enter(1)
        self.queue.enter(2)
        self.queue.enter(3)
        self.assertEqual(self.queue.size(), 3)

    def test_remove_from_queue(self):

        # add two items
        self.queue.enter(1)
        self.queue.enter(2)

        # check the size of queue should be two
        self.assertEqual(self.queue.size(), 2)

        # check that the leave operation provides the correct value
        self.assertEqual(self.queue.leave(), 2)

        # after removing another item
        self.queue.leave()

        # the queue should now be empty
        self.assertEqual(self.queue.size(), 0)

        # an error should be raised when there are no more items to remove
        with self.assertRaises(IndexError):
            self.queue.leave()

    def test_queue_is_empty(self):
        self.assertTrue(self.queue.isEmpty())
        self.queue.enter(1)
        self.assertFalse(self.queue.isEmpty())
        self.queue.leave()
        self.assertTrue(self.queue.isEmpty())


class TestDequeue(unittest.TestCase):

    def setUp(self):
        self.dequeue = Dequeue()

    def test_add_items_to_dequeue_right(self):
        self.assertEqual(self.dequeue.size(), 0)
        self.dequeue.enterRight(1)
        self.dequeue.enterRight(2)
        self.dequeue.enterRight(3)
        self.assertEqual(self.dequeue.size(), 3)

    def test_remove_from_dequeue_right(self):

        # add two items
        self.dequeue.enterRight('r1')
        self.dequeue.enterRight('r2')

        # check the size of queue should be two
        self.assertEqual(self.dequeue.size(), 2)

        # check that the leave operation provides the correct value
        self.assertEqual(self.dequeue.leaveRight(), 'r2')

        # after removing another item
        self.dequeue.leaveRight()

        # the queue should now be empty
        self.assertEqual(self.dequeue.size(), 0)

        # an error should be raised when there are no more items to remove
        with self.assertRaises(IndexError):
            self.dequeue.leaveRight()

    def test_add_items_to_dequeue_left(self):
        self.assertEqual(self.dequeue.size(), 0)
        self.dequeue.enterLeft(1)
        self.dequeue.enterLeft(2)
        self.dequeue.enterLeft(3)
        self.assertEqual(self.dequeue.size(), 3)

    def test_remove_from_dequeue_left(self):

        # add two items
        self.dequeue.enterLeft('l1')
        self.dequeue.enterLeft('l2')

        # check the size of queue should be two
        self.assertEqual(self.dequeue.size(), 2)

        # check that the leave operation provides the correct value
        self.assertEqual(self.dequeue.leaveLeft(), 'l2')

        # after removing another item
        self.dequeue.leaveLeft()

        # the queue should now be empty
        self.assertEqual(self.dequeue.size(), 0)

        # an error should be raised when there are no more items to remove
        with self.assertRaises(IndexError):
            self.dequeue.leaveLeft()

    def test_enter_and_leave_dequeue_both_sides(self):
        self.dequeue.enterLeft('l1')
        self.dequeue.enterRight('r1')
        self.assertEqual(self.dequeue.size(), 2)
        self.dequeue.enterRight('r2')
        self.dequeue.enterLeft('l2')
        self.dequeue.leaveLeft()
        self.dequeue.leaveLeft()
        self.dequeue.leaveLeft()
        self.assertEqual(self.dequeue.leaveRight(), 'r2')

        with self.assertRaises(IndexError):
            self.dequeue.leaveRight()


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linkedL = LinkedList()

    def test_adding_items_to_list(self):
        self.linkedL.append(13)
        self.linkedL.append(23)
        self.linkedL.append(100)
        self.assertEqual(self.linkedL.length(), 3)
        self.assertEqual(self.linkedL.get(0), 13)
        self.assertEqual(self.linkedL.get(1), 23)
        self.assertEqual(self.linkedL.get(2), 100)
        # TODO: raise errors instead of -1
        with self.assertRaises(IndexError):
            self.linkedL.get(-23)
        with self.assertRaises(IndexError):
            self.linkedL.get(10)

    def test_search_for_items(self):
        self.linkedL.append(1)
        self.linkedL.append(100)
        self.linkedL.append(42)

        self.assertTrue(self.linkedL.has(1))
        self.assertTrue(self.linkedL.has(100))
        self.assertTrue(self.linkedL.has(42))

        self.assertFalse(self.linkedL.has(2))

    def test_append_item(self):
        self.linkedL.insert(0, 1)
        self.assertEqual(self.linkedL.get(0), 1)
        self.linkedL.insert(1, 2)
        self.assertEqual(self.linkedL.get(1), 2)
        self.linkedL.insert(0, 3)
        self.assertEqual(self.linkedL.get(0), 3)
        self.linkedL.append(8)
        self.linkedL.append(5)
        self.linkedL.append(11)
        self.linkedL.insert(45, 18)
        self.assertEqual(self.linkedL.get(6), 18)

    def test_remove_items(self):
        self.linkedL.append('a')
        self.linkedL.append('b')
        self.linkedL.append('c')
        self.linkedL.append('d')
        self.assertEqual(self.linkedL.pop(), 'd')
        self.assertEqual(self.linkedL.pop(), 'c')
        self.assertEqual(self.linkedL.pop(), 'b')
        self.assertEqual(self.linkedL.pop(), 'a')
        with self.assertRaises(OverflowError):
            self.linkedL.pop()

    def test_romve_item_by_pos(self):
        self.linkedL.add(1)
        self.linkedL.add(2)
        self.linkedL.add(3)
        self.linkedL.add(4)
        item = self.linkedL.pop(pos=0)
        self.assertEqual(self.linkedL.length(), 3)
        self.assertEqual(item, 4)
        item = self.linkedL.pop(pos=2)
        self.assertEqual(self.linkedL.length(), 2)
        self.assertEqual(item, 1)
        item = self.linkedL.pop(pos=1)
        self.assertEqual(self.linkedL.length(), 1)

    def test_add_item(self):
        self.assertEqual(self.linkedL.length(), 0)
        self.linkedL.add(1)
        self.linkedL.add(2)
        self.linkedL.add(3)
        self.assertEqual(self.linkedL.length(), 3)
        self.assertEqual(self.linkedL.get(2), 1)
        self.assertEqual(self.linkedL.get(0), 3)


if __name__ == '__main__':
    unittest.main()
