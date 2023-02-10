import matplotlib.pyplot as plt
from GraphHelper import PrintGraph

class InvalidGraphException(Exception):
    "To be raised if a Graph is not of the right type"
    pass

class Graph:
    def __init__(self, node_dict: dict, connections: dict, directed=False):
        "Class to create a Graph can be directed or undirected"
        self.node_dict = node_dict
        self.connections = connections
        self.directed = directed
    
    def nodes(self):
        return list(self.connections.keys())
    
    def neighbors(self, node):
        return list(self.connections[node].keys())
    
    def return_edge_weight(self, node1, node2):
        return self.connections.get(node1).get(node2, 0)
    
    def all_edges(self):
        all_edges = set()
        for edge_start in self.nodes():
            for edge_end in self.neighbors(edge_start):
                if self.directed:
                    all_edges.add((edge_start, edge_end, self.connections[edge_start][edge_end]))
                else:
                    all_edges.add(((min(edge_start, edge_end)), max(edge_start, edge_end), self.connections[edge_start][edge_end]))
        return list(all_edges)
    
    def is_joined(self, node1, node2):
        return node2 in self.connections[node1]
    
    def add_node(self, node_name, node_dict={}):
        self.node_dict[node_name] = node_dict
        self.connections[node_name] = {}
    
    def add_edge(self, node1, node2, weight=1):
        node1_connections = self.connections.get(node1)
        node1_connections.update({node2: weight})
        self.connections.update({node1: node1_connections})
        if not self.directed:
            node2_connections = self.connections.get(node2)
            node2_connections.update({node1: weight})
            self.connections.update({node2: node2_connections})
    
    def remove_edge(self, node1, node2):
        del self.connections[node1][node2]
        if not self.directed:
            del self.connections[node2][node1]
    
    def remove_node(self, node):
        node_connections = self.connections[node]
        for connected_node in set(node_connections):
            del self.connections[node][connected_node]
            del self.connections[connected_node][node]
        del self.connections[node]
        del self.node_dict[node]
    
    def is_connected(self, start=None, visited=None):
        node_lst = self.nodes()
        if start is None:
            start = node_lst[0]
        if visited is None:
            visited = set()
        visited.add(start)
        if len(visited) != len(node_lst):
            for neighboring_node in self.neighbors(start):
                if neighboring_node not in visited:
                    if self.is_connected(neighboring_node, visited):
                        return True
        else:
            return True
        return False

    def is_cyclic(self):
        
        def _contains_cycle(graph, node_lst, current_node, visited, parent_node):
            visited.add(current_node)
            for neighboring_node in graph.neighbors(current_node):
                if neighboring_node not in visited:
                    if _contains_cycle(graph, node_lst, neighboring_node, visited, current_node):
                        return True
                elif parent_node != neighboring_node:
                    return True
            return False

        node_lst = self.nodes()
        visited = set()
        for node in node_lst:
            if not node in visited:
                if _contains_cycle(self, node_lst, node, visited, None):
                    return True
        return False
    
    def kruskal(self):
        try:
            check = self.directed
            if check:
                raise InvalidGraphException
            else:
                kruskal = Graph({}, {}, self.directed)
                for node, node_info in self.node_dict.items():
                    kruskal.add_node(node, node_info)
                print("nodes in kruskal:", str(kruskal.nodes()))
                queue = sorted(self.all_edges(), key=lambda edge: edge[2])
                print("queue for sorting:", queue)
                connectedBool = False
                while len(queue) != 0 or connectedBool:
                    edge = queue.pop(0)
                    print("edge to add:", edge)
                    begin, end, weight = edge
                    kruskal.add_edge(begin, end, weight)
                    if kruskal.is_cyclic():
                        print("edge not added because it is cyclic")
                        kruskal.remove_edge(begin, end)
                    if kruskal.is_connected():
                        connectedBool = True
                min_weight = 0
                for edge in kruskal.all_edges():
                    min_weight += edge[2]
                
                return min_weight, kruskal

        except InvalidGraphException:
            print("This method only works for undirected Graphs")

        


if __name__ == "__main__":
    
    nodes = {'v0': {'pos': [3.0, 2.0], 'color': 'cyan'},
    'v1': {'pos': [2.0, 1.5], 'color': 'orange'},
    'v2': {'pos': [3.0, 3.5], 'color': 'orange'},
    'v3': {'pos': [3.5, 2.6], 'color': 'grey'},
    'v4': {'pos': [3.5, 5.5], 'color': 'orange'},
    'v5': {'pos': [2.5, 3.5], 'color': 'blue'},
    'v6': {'pos': [1.5, 2.5], 'color': 'red'},
    'v7': {'pos': [4.0, 2.0], 'color': 'pink'}
    }
    connections = {'v0': {'v1': 2, 'v2': 1, 'v6': 2, 'v7': 1},
    'v1': {'v0': 2},
    'v2': {'v0': 1, 'v3': 1, 'v4': 2, 'v6': 3},
    'v3': {'v2': 1, 'v4': 1},
    'v4': {'v2': 2, 'v3': 1, 'v6': 1},
    'v5': {'v6': 1},
    'v6': {'v0': 2, 'v2': 3, 'v4': 1, 'v5': 1},
    'v7': {'v0': 1}
    }


    g = Graph(nodes, connections)
    print(f"all the nodes: {str(g.nodes())}")
    print(f"all edges on the graph: {str(g.all_edges())}")
    PrintGraph(g, "Graph with 8 nodes")
    g.add_edge('v1', 'v2', weight=2)
    g.add_node('v8', {'pos': [1.4, 0.8], 'color': 'purple'})
    g.add_edge('v8', 'v7', 3)
    g.add_edge('v8', 'v1', 1)
    g.remove_edge('v1', 'v2')
    PrintGraph(g, "Graph with 9 nodes")
    print(f"The graph is connected: {g.is_connected('v1')}")
    print(f"The graph is cyclic: {g.is_cyclic()}")
    weight, kruskal = g.kruskal()
    PrintGraph(kruskal, f"Graph with minimum weight of {weight}")

