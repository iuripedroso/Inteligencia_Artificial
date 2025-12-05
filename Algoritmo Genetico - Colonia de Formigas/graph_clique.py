import numpy as np

class Graph:
    def __init__(self, adjacency_matrix):
        self.adjacency = adjacency_matrix
        self.num_nodes = len(adjacency_matrix)
        
        # Feromônios: Um valor para cada NÓ (vértice)
        self.pheromones = np.ones(self.num_nodes)
        
        # Heurística (η): Um "chute" inicial. 
        # Vamos usar o "grau" de cada nó (quantas conexões ele tem).
        # Nós com mais conexões são, a princípio, melhores candidatos.
        self.heuristic = np.sum(adjacency_matrix, axis=1)
        
        # Evitar divisão por zero se um nó for isolado
        self.heuristic[self.heuristic == 0] = 1e-10