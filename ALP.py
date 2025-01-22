import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight=1):
        self.graph.add_edge(node1, node2, weight=weight)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw(self.graph, pos, with_labels=True, node_color='skyblue', node_size=700)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)
        plt.show()

    def shortest_path(self, start, end):
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            return path
        except nx.NetworkXNoPath:
            return f"No path between {start} and {end}"

    def visual_shortest_path(self, start, end):
        path = self.shortest_path(start, end)
        if isinstance(path, list):
            subgraph = self.graph.subgraph(path)
            pos = nx.spring_layout(self.graph)
            nx.draw(self.graph, pos, with_labels=True, node_color='lightgray', node_size=700)
            nx.draw(subgraph, pos, with_labels=True, edge_color='red', node_color='skyblue', node_size=700)
            plt.show()
        else:
            print(path)

    def is_connected(self):
        return nx.is_connected(self.graph)

    def node_degree(self, node):
        return self.graph.degree(node)

    def get_all_paths(self, start, end):
        return list(nx.all_simple_paths(self.graph, source=start, target=end))

    def total_weight(self):
        return sum(d['weight'] for (u, v, d) in self.graph.edges(data=True))

    def clustering_coefficient(self, node=None):
        if node:
            return nx.clustering(self.graph, node)
        return nx.clustering(self.graph)

graph = Graf()
graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)

graph.visualize_graph()

print("Jalur terpendek dari 1 ke 5:", graph.shortest_path(1, 5))
graph.visual_shortest_path(1, 5)
print("Apakah graf terhubung?", graph.is_connected())
print("Derajat node 3:", graph.node_degree(3))
print("Semua jalur dari 1 ke 5:", graph.get_all_paths(1, 5))
print("Total bobot graf:", graph.total_weight())
print("Koefisien klastering:", graph.clustering_coefficient())
