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
    
    def __str__(self):
        return_string = "|-"
        for item in self:
            return_string += f"{item}-"
        return return_string + "|"

    def enqueue(self, item):
        if item is not None:
            ToEnqueue = Node(item)
            if self.__head is None:
                self.__head = ToEnqueue

            elif self.__tail is None:
                self.__head.next = ToEnqueue
                self.__tail = ToEnqueue

            else:
                self.__tail.next = ToEnqueue
                self.__tail = ToEnqueue

            self.__size += 1
    
    def dequeue(self):
        if self.empty():
            return None
        else:
            node = self.__head
            if node.next is not None:
                nextnode = node.next
                self.__head = nextnode
                self.__size -= 1
                return node.data
            else:
                self.__head = None
                self.__tail = None
                self.__size -= 1
                return node.data

if __name__ == "__main__":
    q = Queue()
    print(q)

    lst = [Node(i) for i in range(10)]
    for node in lst:
        q.enqueue(node)
    
    print(q)
    print(f"length of queue after adding: {len(q)}")

    while not q.empty():
        dequeuedNode = q.dequeue()
        print(f"node taken: {dequeuedNode}, queue now: {q} with length of {len(q)}")


