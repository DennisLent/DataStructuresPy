import DLL
import unittest

class TestDLL(unittest.TestCase):

    def test_create(self):
        dll = DLL.DoublyLinkedList()
        self.assertIsInstance(dll, DLL.DoublyLinkedList)
    
    def test_length(self):
        dll = DLL.DoublyLinkedList()
        self.assertEqual(0, len(dll))
    
    def test_add(self):
        dll = DLL.DoublyLinkedList()
        dll.add(1)
        dll.add(2)
        self.assertEqual(2, len(dll))


if __name__ == "main":
    unittest.main()

