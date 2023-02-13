import matplotlib.pyplot as plt
from GraphHelper import PrintGraph

class InvalidGraphException(Exception):
    "To be raised if a Graph is not of the right type"
    pass

class NotConnectedException(Exception):
    "Raised if a tree is not connected"
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
            if not self.is_connected():
                raise NotConnectedException
            else:
                kruskal = Graph({}, {}, self.directed)
                for node, node_info in self.node_dict.items():
                    kruskal.add_node(node, node_info)
                queue = sorted(self.all_edges(), key=lambda edge: edge[2])
                connectedBool = False
                while ((len(queue) != 0) or (not connectedBool)):
                    edge = queue.pop(0)
                    begin, end, weight = edge
                    kruskal.add_edge(begin, end, weight)
                    if kruskal.is_cyclic():
                        kruskal.remove_edge(begin, end)
                    if kruskal.is_connected():
                        connectedBool = True
                min_weight = 0
                for edge in kruskal.all_edges():
                    min_weight += edge[2]
                
                return min_weight, kruskal

        except InvalidGraphException:
            print("This method only works for undirected Graphs")
        
        except NotConnectedException:
            print("The graph is connected")
    
    def bellmanFord(self, start_node):
        nodes = self.nodes()
        distances = {}
        for node in nodes:
            distances[node] = float("Inf")
        distances[start_node] = 0
        for _ in range(len(nodes)-1):
            for edge in self.all_edges():
                begin, end, weight = edge
                if distances[begin] + weight < distances[end]:
                    distances[end] = distances[begin] + weight
        for _ in range(len(nodes)-1):
            for edge in self.all_edges():
                begin, end, weight = edge
                if distances[begin] + weight < distances[end]:
                    distances[end] = float("-Inf")
        return distances 



        


if __name__ == "__main__":

    import random
    
    def generateRandomGraph(n_nodes: int, max_connections_per_node: int, max_weight = 1, directed=False, random_color=False, dim=(100,100)):
            graph = Graph({}, {}, directed)
            for i in range(n_nodes + 1):
                pos = [random.randrange(0,dim[0]), random.randrange(0,dim[1])]
                if random_color:
                    color = (random.random(), random.random(), random.random())
                    node_dict = {"pos": pos, "color": color}
                else:
                    node_dict = {"pos": pos, "color": "black"}
                graph.add_node(f"v{i}", node_dict)
            for start_node in graph.nodes():
                for _ in range(random.randrange(max_connections_per_node)+1):
                    end_index = random.randrange(0, n_nodes+1)
                    end_node = graph.nodes()[end_index]
                    weight = random.randint(1, max_weight)
                    if start_node != end_node:
                        graph.add_edge(start_node, end_node, weight)
            return graph
    

    g = generateRandomGraph(10, 3, 5)
    print(f"all the nodes: {str(g.nodes())}")
    print(f"all edges on the graph: {str(g.all_edges())}")
    PrintGraph(g, f"Random Graph with {len(g.nodes())} nodes")
    print(f"The graph is connected: {g.is_connected('v1')}")
    print(f"The graph is cyclic: {g.is_cyclic()}")
    weight, kruskal = g.kruskal()
    PrintGraph(kruskal, f"Graph with {len(kruskal.nodes())} minimum weight of: {weight}")

    for node in g.nodes():
        dist = g.bellmanFord(node)
        print(f"-----Minimum distances from {node}-----")
        for end_node, weight in dist.items():
            print(f"{node} to {end_node} = {weight}")

