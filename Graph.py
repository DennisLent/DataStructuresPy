import matplotlib.pyplot as plt
from GraphHelper import PrintGraph

class Graph:
    def __init__(self, nodes: dict, connections: dict, directed=False):
        "Class to create a Graph can be directed or undirected"
        self.nodes = nodes
        self.connections = connections
        self.directed = directed
        self.node_list = list(nodes.keys())

    def nodes(self):
        return self.node_list

    def add_node(self, node_id, location, color):
        self.nodes[node_id] = [location, color]
        self.connections[node_id] = {}

    def remove_node(self, node_id):
        if node_id in self.nodes.keys():
            del self.nodes[node_id]
            del self.connections[node_id]
            for node in self.connections:
                if node_id in self.connections[node]:
                    del self.connections[node][node_id]

    def add_edge(self, begin_node, end_node, weight):
        if begin_node in self.nodes and end_node in self.nodes:
                self.connections[begin_node][end_node] = weight
                if not self.directed:
                    self.connections[end_node][begin_node] = weight

    def remove_edge(self, begin_node, end_node):
        if begin_node in self.nodes and end_node in self.nodes:
            del self.connections[begin_node][end_node]
            if not self.directed:
                del self.connections[end_node][begin_node]

    def change_edge_weight(self, begin_node, end_node, new_weight):
        if begin_node in self.nodes and end_node in self.nodes:
            self.connections[begin_node][end_node] = new_weight
            if not self.directed:
                self.connections[end_node][begin_node] = new_weight

    def is_connected(self, start=None, visited=None):
        if start is None:
            start = self.node_list[0]
        if visited is None:
            visited = set()
        visited.add(start)
        if len(visited) != len(self.node_list):
            neighbors = self.connections[start].keys()
            for neighbor in neighbors:
                if neighbor not in visited:
                    if self.is_connected(neighbor, visited):
                        return True
        else:
            return True

        return False

    def is_cyclic(self, node, visited, parent=None):
        visited.add(node)
        for neighbor in self.connections[node].keys():
            if neighbor not in visited:
                if self.is_cyclic(neighbor, visited, node):
                    return True
            elif parent != neighbor:
                return True
        return False

    def all_edges(self):
        edges = set()
        if self.directed:
            for begin, connection in self.connections.items():
                for end, weight in connection.items():
                    edges.add((begin, end, weight))
        else:
            for begin, connection in self.connections.items():
                for end, weight in connection.items():
                    if begin < end:
                        edges.add((begin, end, weight))
        return list(edges)

    def Kruskal(self):
        queue = sorted(self.all_edges(), key=lambda edge: edge[2])
        #print(f"THIS IS THE QUEUE {queue}")

        graph = Graph(self.nodes, {}, self.directed)
        #print(f"THESE ARE THE NODES {self.node_list}")

        while len(queue) != 0:
            con = queue[0]
            graph.add_edge(con[0], con[1], con[2])
            if graph.is_cyclic(con[0], set(), parent=None):
                graph.remove_edge(con[0], con[1])

            if graph.is_connected():
                PrintGraph(graph)
            else:
                queue.pop(0)