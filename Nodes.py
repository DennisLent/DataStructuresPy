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
    def __init__(self, data: Any, key: str, next=None, prev=None):
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


if __name__ == "__main__":
    NodeWorks = Node2(3, "test")
    NodeFails = Node2(3, 5)