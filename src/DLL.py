from src import Nodes


class DoublyLinkedList:
    """
    Doubly Linked List that is none terminated
    Empty if head and tail are None
    Takes in None or a list
    """
    def __init__(self, lst=[]):
            self.__head = None
            self.__tail = None
            self.__size = 0
            if lst is not None:
                for item in lst:
                    self.add(item)

    def __str__(self):
        return_string = "|"
        node = self.get_first()
        while node is not None:
            return_string += f"-{node}"
            node = node.next
        return return_string + "|"

    def __len__(self):
        return self.__size

    def __min__(self):
        return self.smallest()

    def __max__(self):
        return self.greatest()

    def get_first(self):
        return self.__head

    def get_last(self):
        return self.__tail

    def empty(self):
        return self.__head is None and self.__tail is None

    def size(self):
        return self.__size

    def add(self, item):
        if item is not None:
            node = Nodes.Node(item)
            if self.empty():
                self.__head = node
            else:
                node.prev = self.__tail
                self.__tail.next = node
            self.__tail = node
            self.__size += 1

    def __iter__(self):
        self.__current = self.get_first()
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration()

        result = self.__current
        self.__current = self.__current.next
        return result

    def search(self, key):
        result = None
        for node in self:
            if key == node.data:
                result = node
        return result

    def remove(self, key):
        node = self.search(key)
        if node is not None:
            prev_node = node.prev
            next_node = node.next

            if prev_node is not None:
                prev_node.next = next_node
            else:
                self.__head = next_node

            if next_node is not None:
                next_node.prev = prev_node
            else:
                self.__tail = prev_node

            self.__size -= 1

    def smallest(self):
        sml = self.get_first()
        for item in self:
            if item < sml:
                sml = item
        return sml.data

    def greatest(self):
        grt = self.get_first()
        for item in self:
            if item > grt:
                grt = item
        return grt.data

if __name__ == "__main__":
    pass


