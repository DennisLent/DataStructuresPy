import matplotlib.pyplot as plt
from GraphHelper import PrintGraph

class Graph:
    def __init__(self, node_dict: dict, connections: dict, directed=False):
        "Class to create a Graph can be directed or undirected"
        self.node_dict = nodes
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
        self.nodes[node_name] = node_dict
        self.connections = {}
    
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


    g = Graph(nodes, connections, True)
    print(f"all the nodes: {str(g.nodes())}")
    print(f"all edges on the graph: {str(g.all_edges())}")
    PrintGraph(g)

