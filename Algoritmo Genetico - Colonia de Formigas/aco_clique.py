# aco_clique.py
import numpy as np
from ant_clique import Ant # Importa a classe do arquivo vizinho

class ACO:
    def __init__(self, graph, num_ants, num_iterations, decay=0.5, deposit_strength=1.0):
        self.graph = graph
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.decay = decay # Taxa de evaporação (ρ)
        self.deposit_strength = deposit_strength # 'alpha' do PDF (source 58)
        
        # Para o gráfico de convergência
        self.best_size_history = [] 

    def _update_pheromones(self, ants):
        """
        Atualiza os feromônios nos NÓS.
        """
        # 1. Evaporação (como no PDF, source 78)
        self.graph.pheromones *= self.decay
        
        # 2. Depósito
        for ant in ants:
            # O "prêmio" é o tamanho da clique que a formiga achou
            # (Equivalente ao `1 / ant.total_distance` do PDF)
            reward = ant.clique_size 
            
            # Deposita o prêmio em cada NÓ que fez parte daquela clique
            for node in ant.clique:
                self.graph.pheromones[node] += self.deposit_strength * reward

    def run(self):
        """
        Executa o algoritmo principal.
        """
        best_clique = None
        best_clique_size = 0 # Objetivo é MAXIMIZAR, começa em 0
        
        print("Iniciando otimização ACO para Problema do Clique...")
        
        for i in range(self.num_iterations):
            # Cria um novo "exame" de formigas
            ants = [Ant(self.graph) for _ in range(self.num_ants)]
            
            for ant in ants:
                ant.build_clique() # Cada formiga constrói sua solução
                
                # Verifica se essa formiga achou uma solução melhor que a global
                if ant.clique_size > best_clique_size:
                    best_clique_size = ant.clique_size
                    best_clique = ant.clique
            
            # Atualiza os feromônios com base no desempenho de todas as formigas
            self._update_pheromones(ants)
            
            # Salva o melhor resultado da iteração para o gráfico
            self.best_size_history.append(best_clique_size)
            
            if (i+1) % 10 == 0:
                print(f"Iteração {i+1}/{self.num_iterations} | Melhor Clique: {best_clique_size} nós")
        
        print("Otimização concluída.")
        return best_clique, best_clique_size