class Node:
    """
    Basic Node structure
    """
    def __init__(self, data, next=None, prev=None):
        self.__data = data
        self.__next = next
        self.__prev = prev

    def __str__(self):
        return f"{self.__data}"

    def get_next(self):
        return self.__next

    def set_next(self, item):
        self.__next = item

    def get_prev(self):
        return self.__prev

    def set_prev(self, item):
        self.__prev = item

    def get_data(self):
        return self.__data

    def set_data(self, item):
        self.__data = item

    next = property(get_next, set_next)

    prev = property(get_prev, set_prev)

    data = property(get_data, set_data)

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

class InvalidKeyException(Exception):
    "Raised when key is not a string"
    pass

class Node2:
    """
    Basic Node structure for Hashmap
    """
    def __init__(self, data, key, next=None, prev=None):
        try:
            self.__key = key
            if not type(key) == str:
                raise InvalidKeyException
            else:
                self.__data = data
                self.__next = next
                self.__prev = prev
        except InvalidKeyException:
            print("key should be a string")

    def __str__(self):
        return f"({self.__key}): {self.__data}"

    def get_next(self):
        return self.__next

    def set_next(self, item):
        self.__next = item

    def get_prev(self):
        return self.__prev

    def set_prev(self, item):
        self.__prev = item

    def get_data(self):
        return self.__data

    def set_data(self, item):
        self.__data = item
    
    def get_key(self):
        return self.__key

    def set_key(self, item):
        self.__key = item

    next = property(get_next, set_next)

    prev = property(get_prev, set_prev)

    data = property(get_data, set_data)

    key = property(get_key, set_key)

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

class BSTNode:
    """
    Basic Node structure for binary tree
    """
    def __init__(self, data, left=None, right=None):
        self.__data = data
        self.__left = left
        self.__right = right

    def __str__(self):
        return f"{self.__data}"

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


if __name__ == "__main__":
    NodeWorks = Node2(3, "test")
    NodeFails = Node2(3, 5)