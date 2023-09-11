# DataStructuresPy
Repo for basic data structures
The idea for this was taken from [GoDaddy](https://in.godaddy.com/blog/8-basic-data-structures-every-programmer-should-know/#:~:text=Arrays%2C%20linked%20lists%2C%20stacks%2C,are%20the%20basic%20data%20structures.) Which gives a more explicit overview of each data structure. Also keep in mind, these implementations might not be the best (as in the _most efficient_) but serve to help outline the basic idea behind data structures and how to go about coding them. 

## Nodes
Includes functionality for nodes that are used throughout the data structures. Nodes2 is only used for the hashamp as it includes the key attribute which is necessary

## DoublyLinkedList
> A linked list is a linear data structure where items are arranged in linear order and linked (connected) to each other.

Functionalities include:
- adding / removing elements
- searching for elements
- returning smallest and greatest elements
- iteration

The items in the linked list are in a node. This means that to access the specific data stored in them, you need to access it.
```AssertEqual(Node(1), 1)```
Will fail

## Stack
> Stack is also a linear order structure, but it works in a LIFO (Last in First Out) order. It means the last-placed element can be accessed first.

Functionalities include:
- pushing
- popping
- determening length of stack
- iteration


## Queue
> Queues are the same as Stack structure, but they don’t follow the LIFO model. A queue follows the FIFO (First in First Out) model. This means the first element can be accessed first.

Functionalities include:
- enqueueing
- dequeuing
- determening length of queue
- iteration

## HashMap
> The hash table data structure connects each value with a key and stores them. To map any size of data set to one fixed size, the hash table uses the hash function. The values returned by a hash function are known as hash values

Functionalities include:
- inserting / removing data
- looking for data
- setting and changing the hash function

## Binary Search Tree (BinaryTree)
> In the tree structure, data is linked together as in the linked list but organized hierarchically. As such they are very good for organizing unstructured data and are widely used to help create expression solvers and in wireless networking

Functionalities include:
- inserting
- searching
- in order traversal

## Graph
> A graph is an abstract data structure that consists of a fixed set of nodes (vertices) and is connected by a set of edges (lines connecting the nodes). Graphs are great utensils for solving real-world problems as well as representing digital networks.

_The GraphHelper script includes the necessary function to print the graph and to visualize it. It requires pyplot to work_
_The main function will generate a random graph for testing purposes_

Functionalities include:
- making directed and undirected graphs
- adding and removing edges
- altering edge weights
- checking if the graph is connected
- checking if the graph is cyclic
- kruskal's algorithm: determening the minimum spanning tree necessary to cover all nodes
- dijkstra's algorithm for finding the shortest route to all nodes

## Code Coverage
Make sure coverage is installed
```python3 -m pip install coverage```

You can then just run the coverage results as you would using unittest

```coverage run -m unittest discover -v```
```coverage report ```

Additionally, this will be saved in as a html document, and you can view the entire report in your favorite browser

```firefox htmlcov/index.html```


