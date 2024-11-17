import unittest
from src.LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_append(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        self.assertEqual(ll.display(), [10, 20])

    def test_prepend(self):
        ll = LinkedList()
        ll.append(20)
        ll.prepend(10)
        self.assertEqual(ll.display(), [10, 20])

    def test_delete(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        ll.delete(20)
        self.assertEqual(ll.display(), [10, 30])

    def test_display_empty(self):
        ll = LinkedList()
        self.assertEqual(ll.display(), [])

if __name__ == "__main__":
    unittest.main()
