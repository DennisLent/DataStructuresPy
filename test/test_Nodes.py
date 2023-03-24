import unittest
from src import Nodes

class Test_Nodes(unittest.TestCase):

    def Node_connects(self):
        Node1 = Nodes.Node(1)
        Node2 = Nodes.Node(2)
        Node1.next = Node2
        self.assertEqual(Node1.next, Node2)


if __name__ == "main":
    unittest.main()