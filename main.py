class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, directed=False):
        self.graph[u][v] = 1
        if not directed:
            self.graph[v][u] = 1

    def is_safe(self, v, pos, path):
        if self.graph[path[pos - 1]][v] == 0:  
            return False
        if v in path:  
            return False
        return True

    def hamiltonian_cycle_util(self, path, pos):
        if pos == self.V:
            if self.graph[path[pos - 1]][path[0]] == 1:
                return True
            return False

        for v in range(self.V):
            if self.is_safe(v, pos, path):
                path[pos] = v
                if self.hamiltonian_cycle_util(path, pos + 1):
                    return True
                path[pos] = -1 
        return False

    def find_hamiltonian_cycle(self):
        path = [-1] * self.V
        path[0] = 0 

        if not self.hamiltonian_cycle_util(path, 1):
            print("No Hamiltonian Cycle exists")
            return None
        print("Hamiltonian Cycle found:", path + [path[0]])
        return path

if __name__ == "__main__":
    g = Graph(5)
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 2), (1, 3), (2, 4)]
    for u, v in edges:
        g.add_edge(u, v)

    g.find_hamiltonian_cycle()