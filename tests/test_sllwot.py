import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_structures.linked_list import SinglyLinkedListWithoutTail

class TestSinglyLinkedListWithoutTail(unittest.TestCase):
    def setUp(self):
        self.sll = SinglyLinkedListWithoutTail()

    def test_append(self):
        self.sll.append(1)
        self.sll.append(2)
        self.assertEqual(str(self.sll), "(head) -> 1 -> 2 -> (none)")
        self.assertEqual(self.sll.length(), 2)

    def test_append_complex(self):
        # Append multiple elements
        for i in range(100):
            self.sll.append(i)
        self.assertEqual(str(self.sll), "(head) -> " + " -> ".join(map(str, range(100))) + " -> (none)")
        self.assertEqual(self.sll.length(), 100)

        # Append to an empty list
        self.sll = SinglyLinkedListWithoutTail()
        self.sll.append(999)
        self.assertEqual(str(self.sll), "(head) -> 999 -> (none)")
        self.assertEqual(self.sll.length(), 1)

    def test_prepend(self):
        self.sll.prepend(1)
        self.sll.prepend(0)
        self.assertEqual(str(self.sll), "(head) -> 0 -> 1 -> (none)")
        self.assertEqual(self.sll.length(), 2)

    def test_prepend_complex(self):
        # Prepend multiple elements
        for i in range(100):
            self.sll.prepend(i)
        self.assertEqual(str(self.sll), "(head) -> " + " -> ".join(map(str, reversed(range(100)))) + " -> (none)")
        self.assertEqual(self.sll.length(), 100)

        # Prepend to an empty list
        self.sll = SinglyLinkedListWithoutTail()
        self.sll.prepend(999)
        self.assertEqual(str(self.sll), "(head) -> 999 -> (none)")
        self.assertEqual(self.sll.length(), 1)

    def test_append_and_prepend_combined(self):
        # Combine append and prepend
        self.sll.append(1)
        self.sll.prepend(0)
        self.sll.append(2)
        self.sll.prepend(-1)
        self.assertEqual(str(self.sll), "(head) -> -1 -> 0 -> 1 -> 2 -> (none)")
        self.assertEqual(self.sll.length(), 4)

    def test_append_and_prepend_combined_complex(self):
        # Combine append and prepend with a large number of elements
        for i in range(50):
            self.sll.append(i)
            self.sll.prepend(-i)
        self.assertEqual(self.sll.length(), 100)
        self.assertTrue(str(self.sll).startswith("(head) -> -49 -> -48"))

    def test_edge_cases(self):
        # Append None (should raise ValueError)
        with self.assertRaises(ValueError):
            self.sll.append(None)

        # Prepend None (should raise ValueError)
        with self.assertRaises(ValueError):
            self.sll.prepend(None)

        # Append and prepend to a large list
        for i in range(1000):
            self.sll.append(i)
        self.assertEqual(self.sll.length(), 1000)
        self.sll.prepend(-1)
        self.assertEqual(self.sll.length(), 1001)
        self.assertEqual(str(self.sll).startswith("(head) -> -1 -> 0"), True)

    def test_edge_cases_complex(self):
        # Append None (should raise ValueError)
        with self.assertRaises(ValueError):
            self.sll.append(None)

        # Prepend None (should raise ValueError)
        with self.assertRaises(ValueError):
            self.sll.prepend(None)

        # Append and prepend to a very large list
        for i in range(1000):
            self.sll.append(i)
        self.assertEqual(self.sll.length(), 1000)
        self.sll.prepend(-1)
        self.assertEqual(self.sll.length(), 1001)
        self.assertTrue(str(self.sll).startswith("(head) -> -1 -> 0"))

    def test_insert_after(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.insert_after(1, 1.5)
        self.assertEqual(str(self.sll), "(head) -> 1 -> 1.5 -> 2 -> (none)")
        with self.assertRaises(ValueError):
            self.sll.insert_after(3, 3.5)

    def test_delete_by_key(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.sll.delete_by_key(2)
        self.assertEqual(str(self.sll), "(head) -> 1 -> 3 -> (none)")
        with self.assertRaises(ValueError):
            self.sll.delete_by_key(4)

    def test_delete_by_position(self):
        self.sll.append(1)
        self.sll.append(2)
        self.sll.append(3)
        self.sll.delete_by_position(1)
        self.assertEqual(str(self.sll), "(head) -> 1 -> 3 -> (none)")
        with self.assertRaises(ValueError):
            self.sll.delete_by_position(5)

    def test_traverse(self):
        self.sll.append(1)
        self.sll.append(2)
        self.assertEqual(self.sll.traverse(), ["1", "2"])

    def test_length(self):
        self.assertEqual(self.sll.length(), 0)
        self.sll.append(1)
        self.assertEqual(self.sll.length(), 1)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
