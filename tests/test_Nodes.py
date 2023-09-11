import unittest
from src import Nodes

class Test_Nodes(unittest.TestCase):

    def Node_front_connects(self):
        Node1 = Nodes.Node(1)
        Node2 = Nodes.Node(2)
        Node1.next = Node2
        self.assertEqual(Node1.next, Node2)
    
    def Node_back_connects(self):
        Node1 = Nodes.Node(1)
        Node2 = Nodes.Node(2)
        Node2.prev = Node1
        self.assertEqual(Node2.prev, Node1)

if __name__ == "main":
    unittest.main()