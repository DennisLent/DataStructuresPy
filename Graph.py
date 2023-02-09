import matplotlib.pyplot as plt
from GraphHelper import PrintGraph

class Graph:
    def __init__(self, nodes: dict, connections: dict, directed=False):
        "Class to create a Graph can be directed or undirected"
        self.node_dict = nodes
        self.connections = connections
        self.directed = directed
        self.node_list = list(self.node_dict.keys())

    def nodes(self):
        return list(self.node_dict.keys())

    def add_node(self, node_id, location, color):
        self.node_dict[node_id] = [location, color]
        self.connections[node_id] = {}

    def remove_node(self, node_id):
        if node_id in self.node_dict.keys():
            del self.node_dict[node_id]
            del self.connections[node_id]
            for node in self.connections:
                if node_id in self.connections[node]:
                    del self.connections[node][node_id]

    def add_edge(self, begin_node, end_node, weight):
        if begin_node in self.node_dict and end_node in self.node_dict:
                self.connections[begin_node][end_node] = weight
                if not self.directed:
                    self.connections[end_node][begin_node] = weight

    def remove_edge(self, begin_node, end_node):
        if begin_node in self.node_dict and end_node in self.node_dict:
            del self.connections[begin_node][end_node]
            if not self.directed:
                del self.connections[end_node][begin_node]

    def change_edge_weight(self, begin_node, end_node, new_weight):
        if begin_node in self.node_dict and end_node in self.node_dict:
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
        print("queue:", queue)
        kruskal = Graph(self.node_dict, {}, self.directed)

        print(f"all nodes in the graph: {kruskal.nodes}")

        while len(queue) != 0:
            con = queue[0]
            kruskal.add_edge(con[0], con[1], con[2])
            if kruskal.is_cyclic(con[0], set(), parent=None):
                kruskal.remove_edge(con[0], con[1])

            if kruskal.is_connected():
                return kruskal
            else:
                queue.pop(0)

if __name__ == "__main__":
    nodes = {"v1": [(0,0), "green"],
    "v2": [(1,1), "blue"],
    "v3": [(2,0), "black"],
    "v4": [(0,-4), "pink"],
    "v5": [(-1,0), "yellow"],
    "v6": [(3,3), "brown"],
    "v7": [(2.5, 3), "orange"],
         }
    connections = {"v1": {"v2": 1},
    "v2": {"v3": 1, "v4": 2},
    "v3": {"v4": 2, "v7": 3},
    "v4": {"v5": 4},
    "v5": {"v2": 1},
    "v7": {"v6": 2}
    }

    g = Graph(nodes, connections, True)
    print(f"All the nodes in the graph: {g.nodes}")
    print(f"Is the graph connected? {g.is_connected()}")
    print(f"Is the graph cyclic? {g.is_cyclic('v1', set())}")
    print(f"All connections of the graph: {g.all_edges()}")
    #PrintGraph(g)
    kruskal = g.Kruskal()
    PrintGraph(kruskal)