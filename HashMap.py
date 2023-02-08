from Nodes import Node2

class HashMap:

    def __init__(self, size):
        self.__size = size
        self.__buckets = [None for _ in range(self.__size + 1)]

    
    def __str__(self):
        return_string  = "|"
        for node in self.__buckets:
            return_string += " ["
            if node is not None:
                while node is not None:
                    return_string += f"{node} "
                    node = node.next
            else:
                return_string += "*"
            return_string += "]"
        return return_string + "|"
    
    def hashfunc(self, key):
        index = 0
        for letter in key:
            index += ord(letter)
        return (index % self.__size)
    
    def insert_data(self, node):
        if node is not None:
            index = self.hashfunc(node.key)
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
            index = self.hashfunc(key)
            iternode = self.__buckets[index]
            while iternode is not None:
                if key == iternode.key:
                    return iternode.data
                iternode = iternode.next
            return f"{key} not found"

                    
    


if __name__ == "__main__":

    hm = HashMap(3)
    print(hm)

    node_lst = [Node2(1, "ab"), Node2(2, "gh"), Node2(3, "zz"), Node2(4, "qq"), Node2(5, "hjq"), Node2(6, "ggwp")]
    for node in node_lst:
        hm.insert_data(node)
    
    print(hm)

    print(hm.get_data("ab"))
    print(hm.get_data("abc"))
    

    
    
    
