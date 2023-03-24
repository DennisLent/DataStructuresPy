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
        if item is not None:
            ToPush = Node(item)
            if self.__head is None:
                self.__head = ToPush
            elif self.__tail is None:
                self.__head.next = ToPush
                self.__tail = ToPush
                self.__tail.prev = self.__head
            else:
                self.__tail.next = ToPush
                ToPush.prev = self.__tail
                self.__tail = ToPush
            self.__size += 1
    
    def pop(self):
        if self.empty():
            return None
        else:
            node = self.__tail
            if node.prev is not None:
                prevnode = node.prev
                self.__tail = prevnode
                self.__tail.next = None
                self.__size -= 1
                return node.data
            else:
                self.__head = None
                self.__tail = None
                self.__size -= 1
                return node.data

if __name__ == "__main__":
    stack = Stack()
    print(stack)

    lst = [Node(i) for i in range(10)]
    for node in lst:
        stack.push(node)
    
    print(stack)
    print(f"length of stack after adding: {len(stack)}")

    while not stack.empty():
        popppedNode = stack.pop()
        print(f"node taken: {popppedNode}, stack now: {stack} with length of {len(stack)}")