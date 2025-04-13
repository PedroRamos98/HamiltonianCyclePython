import networkx as nx
import matplotlib.pyplot as plt
from main import Graph

def visualize_hamiltonian_cycle(graph, path=None):
    G = nx.Graph()
    G.add_nodes_from(range(graph.V))
    
    for i in range(graph.V):
        for j in range(graph.V):
            if graph.graph[i][j] == 1:
                G.add_edge(i, j)

    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=12)
    nx.draw_networkx_edges(G, pos, edge_color='gray')

    
    if path and path[0] != -1:
        hamiltonian_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        if graph.graph[path[-1]][path[0]] == 1: 
            hamiltonian_edges.append((path[-1], path[0]))
        nx.draw_networkx_edges(G, pos, edgelist=hamiltonian_edges, edge_color='red', width=2)

    plt.title("Graph with Hamiltonian Cycle (Red Edges)" if path else "Graph")
    plt.savefig("assets/hamiltonian_cycle.png")
    plt.show()

if __name__ == "__main__":
    g = Graph(5)
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (1, 3), (2, 4)]
    for u, v in edges:
        g.add_edge(u, v)


    path = g.find_hamiltonian_cycle()
    visualize_hamiltonian_cycle(g, path)