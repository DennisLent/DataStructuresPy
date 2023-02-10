import matplotlib.pyplot as plt

def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)

def PrintGraph(graph, name=None):

    """
    Method of visualize the graph created
    :return: plot of the graph
    """
    min_x, max_x, min_y, max_y = 0, 0, 0, 0
    for node in graph.node_dict:
        location, color = graph.node_dict[node]["pos"], graph.node_dict[node]["color"]
        if location[0] < min_x:
            min_x = location[0]
        if location[0] > max_x:
            max_x = location[0]
        if location[1] < min_y:
            min_y = location[1]
        if location[1] > max_y:
            max_y = location[1]
        if type(color) == str: 
            plt.scatter(location[0], location[1], color=color)
        else:
            plt.scatter(location[0], location[1], c=color)
        plt.text(location[0], location[1] + 0.01, f"{node}")
    for node in graph.connections:
        for end_node, weight in graph.connections[node].items():
            begin_x, begin_y = graph.node_dict[node]["pos"]
            end_x, end_y = graph.node_dict[end_node]["pos"]
            if not graph.directed:
                plt.plot([begin_x, end_x], [begin_y, end_y], color="red")
            else:
                dx, dy = end_x-begin_x, end_y-begin_y
                plt.arrow(begin_x, begin_y, dx, dy, color="red", length_includes_head=True, width=0.01)
            avg_x, avg_y = (begin_x + end_x) / 2 + 0.01, (begin_y + end_y) / 2 + 0.01
            plt.text(avg_x, avg_y, f"{weight}")
    if name is not None:
        plt.title(name)
    plt.show()

if __name__ == "__main__":
    pass