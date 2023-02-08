from Nodes import Node2

class HashMap:

    def __init__(self, size, hashfunc):
        self.__size = size
        self.__buckets = [None for _ in range(self.__size + 1)]
        self.__hashfunc = hashfunc

    def __str__(self):
        return_string  = "| "
        for node in self.__buckets:
            return_string += "["
            if node is not None:
                while node is not None:
                    return_string += f"{node} "
                    node = node.next
            else:
                return_string += "*"
            return_string += "]"
        return return_string + " |"
    
    def insert_data(self, node):
        if node is not None:
            index = self.__hashfunc(node.key, self.__size)
            if self.__buckets[index] is None:
                self.__buckets[index] = node
            else:
                iternode = self.__buckets[index]
                while iternode.next is not None:
                    iternode = iternode.next
                iternode.next = node
                node.prev = iternode
    
    def get_data(self, key):
        if key is not None:
            index = self.__hashfunc(key, self.__size)
            iternode = self.__buckets[index]
            while iternode is not None:
                if key == iternode.key:
                    return iternode.data
                iternode = iternode.next
        return f"key: {key} not found"
    
    def remove_data(self, key):
        if key is not None:
            index = self.__hashfunc(key, self.__size)
            iternode = self.__buckets[index]
            if iternode.key == key:
                if iternode.next is not None:
                    self.__buckets[index] = iternode.next
                    self.__buckets[index].prev = None
                else:
                    self.__buckets[index] = None
                return
            
            while iternode is not None:
                if key == iternode.key:
                    nextnode = iternode.next
                    prevnode = iternode.prev
                    prevnode.next = nextnode
                    nextnode.prev = prevnode
                    return
                iternode = iternode.next
        return f"key: {key} not found"

                

if __name__ == "__main__":

    def hashfunc(key, size):
        index = 0
        for letter in key:
            index += ord(letter)
        return (index % size)

    hm = HashMap(3, hashfunc)
    print(hm)

    node_lst = [Node2(1, "ab"), Node2(2, "gh"), Node2(3, "zz"), Node2(4, "qq"), Node2(5, "hjq"), Node2(6, "ggwp"), Node2(7, "car"), Node2(8, "ass"), Node2(9, "chill"), Node2(10, "cheese")]
    for node in node_lst:
        hm.insert_data(node)
    
    print(hm)

    print(hm.get_data("ab"))
    print(hm.get_data("abc"))

    hm.remove_data("gh")
    hm.remove_data("zz")
    hm.remove_data("dennis")
    print(hm)

    

    
    
    
