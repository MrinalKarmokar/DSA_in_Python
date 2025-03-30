import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.stack import StackUsingList

class TestStackUsingList(unittest.TestCase):
    def setUp(self):
        self.stack = StackUsingList()

    def test_push(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(str(self.stack), "[1, 2]")
        self.assertEqual(self.stack.size(), 2)

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.peek(), 1)
        with self.assertRaises(ValueError):
            self.stack = StackUsingList()
            self.stack.peek()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(), 2)
        self.stack.pop()
        self.assertEqual(self.stack.size(), 1)

    def test_edge_cases(self):
        # Push None (should raise ValueError)
        with self.assertRaises(ValueError):
            self.stack.push(None)

        # Pop from an empty stack (should raise ValueError)
        with self.assertRaises(ValueError):
            self.stack.pop()

        # Peek from an empty stack (should raise ValueError)
        with self.assertRaises(ValueError):
            self.stack.peek()

    def test_push_complex(self):
        # Push multiple elements
        for i in range(100):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), 100)
        self.assertEqual(self.stack.peek(), 99)

        # Push to an empty stack
        self.stack = StackUsingList()
        self.stack.push(999)
        self.assertEqual(self.stack.size(), 1)
        self.assertEqual(self.stack.peek(), 999)

    def test_pop_complex(self):
        # Pop multiple elements
        for i in range(100):
            self.stack.push(i)
        for i in reversed(range(100)):
            self.assertEqual(self.stack.pop(), i)
        self.assertTrue(self.stack.is_empty())

        # Pop from an empty stack (should raise ValueError)
        with self.assertRaises(ValueError):
            self.stack.pop()

    def test_push_and_pop_combined_complex(self):
        # Combine push and pop with a large number of elements
        for i in range(50):
            self.stack.push(i)
        for i in reversed(range(25, 50)):
            self.assertEqual(self.stack.pop(), i)
        self.assertEqual(self.stack.size(), 25)

    def test_edge_cases_complex(self):
        # Push None (should raise ValueError)
        with self.assertRaises(ValueError):
            self.stack.push(None)

        # Pop from an empty stack (should raise ValueError)
        with self.assertRaises(ValueError):
            self.stack.pop()

if __name__ == "__main__":
    unittest.main()
