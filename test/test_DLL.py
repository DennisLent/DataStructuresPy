import unittest
from src import DLL

class Test_DLL(unittest.TestCase):

    def test_create_empty(self):
        dll = DLL.DoublyLinkedList()
        self.assertEqual(len(dll), 0)

if __name__ == "main":
    unittest.main()