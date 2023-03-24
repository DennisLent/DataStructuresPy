import unittest
from src import DLL

class Test_DLL(unittest.TestCase):

    def test_create_empty(self):
        dll = DLL.DoublyLinkedList()
        self.assertEqual(len(dll), 0)
    
    def test_add(self):
        dll = DLL.DoublyLinkedList()
        dll.add(1)
        self.assertEqual(len(dll), 1)
    
    def test_str_empty(self):
        dll = DLL.DoublyLinkedList()
        self.assertEqual("||", str(dll))
    
    def test_str_not_empty(self):
        dll = DLL.DoublyLinkedList()
        dll.add(1)
        dll.add(2)
        self.assertEqual("|-1-2|", str(dll))


if __name__ == "main":
    unittest.main()