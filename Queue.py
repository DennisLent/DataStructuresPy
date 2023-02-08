from Nodes import Node

class Queue:
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

    def enqueue(self, item):
        if item is not None:
            if self.__head is None:
                self.__head = item

            elif self.__tail is None:
                self.__head.next = self.__tail
                self.__tail = item

            else:
                self.__tail.next = item
                item = self.__tail

            self.__size += 1
    
    def dequeue(self):
        if self.empty():
            return None
        else:
            node = self.__head
            nextnode = self.__head.next
            self.__head = nextnode
            return node

if __name__ == "__main__":
    pass
