from Nodes import BSTNode

class BinaryTree:
    """
    Basic Node structure for binary tree where:
    left child <= parent
    right child > parent 
    """
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def __str__(self):
        return f"|-{self.__data}-|"

    def get_right(self):
        return self.__right

    def set_right(self, item):
        self.__right = item

    def get_left(self):
        return self.__left

    def set_left(self, item):
        self.__left = item

    def get_data(self):
        return self.__data

    def set_data(self, item):
        self.__data = item

    right = property(get_right, set_right)

    left = property(get_left, set_left)

    data = property(get_data, set_data)

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data
    
    def insert(self, key):
        if key <= self.data:
            if self.left is None:
                self.left = BinaryTree(key)
            else:
                self.left.insert(key)
        if key > self.data:
            if self.right is None:
                self.right = BinaryTree(key)
            else:
                self.right.insert(key)
    


if __name__ == "__main__":
    pass