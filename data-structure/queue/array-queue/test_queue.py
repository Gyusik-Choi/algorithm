from unittest import TestCase
import queue


class TestQueue(TestCase):
    def setUp(self):
        self.queue = queue.Queue(3)

    def test_push(self):
        self.queue.push(1)
        self.assertEqual(self.queue.end, 1)

    def test_push_2(self):
        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)
        self.queue.push(4)
        self.queue.push(5)

        self.assertEqual(self.queue.front(), 1)
        self.assertEqual(self.queue.rear(), 3)

    def test_pop(self):
        self.queue.push(1)
        self.queue.push(2)
        self.queue.push(3)

        self.assertEqual(self.queue.pop(), 1)
        self.assertEqual(self.queue.pop(), 2)
        self.assertEqual(self.queue.pop(), 3)

        self.assertEqual(self.queue.pop(), None)

    def test_front(self):
        self.assertEqual(self.queue.front(), None)

        self.queue.push(1)
        self.assertEqual(self.queue.front(), 1)

        self.queue.push(2)
        self.assertEqual(self.queue.front(), 1)

    def test_rear(self):
        self.assertEqual(self.queue.rear(), None)

        self.queue.push(1)
        self.assertEqual(self.queue.rear(), 1)

        self.queue.push(2)
        self.assertEqual(self.queue.rear(), 2)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.push(1)
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.push(1)
        self.assertFalse(self.queue.is_full())
        self.queue.push(2)
        self.assertFalse(self.queue.is_full())
        self.queue.push(3)
        self.assertTrue(self.queue.is_full())
        self.queue.push(4)
        self.assertTrue(self.queue.is_full())
        self.queue.push(5)
        self.assertTrue(self.queue.is_full())
