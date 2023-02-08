from Nodes import Node

class Stack:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def empty(self):
        return self.__head is None and self.__tail is None
    
    def __iter__(self):
        self.__current = self.__head
        return self
    
    def __next__(self):
        if self.__current is None:
            raise StopIteration()
        result = self.__current
        self.__current = self.__current.next
        return result
    
    def __str__(self):
        return_string = "|-"
        for item in self:
            return_string += f"{item}-"
        return return_string + "|"

    def push(self, item):
        if self.__head is None:
            self.__head = item
        elif self.__tail is None:
            self.__head.next = item
            self.__tail = item
        else:
            self.__tail.next = item
            self.__tail = item
        self.__size += 1
    
    def pop(self):
        if self.empty():
            return None

if __name__ == "__main__":
    stack = Stack()
