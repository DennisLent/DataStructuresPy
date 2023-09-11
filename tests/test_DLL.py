import unittest
from src import DLL
from tests import *

class Test_DLL(unittest.TestCase):

    def test_create_empty(self):
        dll = DLL.DoublyLinkedList()
        self.assertEqual(len(dll), 0)
    
    def test_create_non_empty(self):
        dll = DLL.DoublyLinkedList([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(dll.get_first().data, 1)
        self.assertEqual(dll.get_last().data, 10)
        self.assertEqual(dll.size(), 10)
    
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

    def test_iter(self):
        dll = DLL.DoublyLinkedList([1,2,3,4,5])
        new_list = []
        for item in dll:
            new_list.append(item.data)
        self.assertEqual(new_list, [1,2,3,4,5])
    
    def test_in_list(self):
        dll = DLL.DoublyLinkedList([1,2,3,4,5])
        found = dll.search(3)
        self.assertEqual(found.data, 3)
    
    def test_not_in_list(self):
        dll = DLL.DoublyLinkedList([1,2,3,4,5])
        not_found = dll.search(20)
        self.assertEqual(not_found, None)
    
    def test_remove(self):
        dll = DLL.DoublyLinkedList([1,2,3,4,5])
        dll.remove(3)
        self.assertEqual(dll.search(3), None)



if __name__ == "main":
    unittest.main()