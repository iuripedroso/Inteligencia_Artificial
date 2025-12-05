import numpy as np

class Ant:
    def __init__(self, graph, alpha=2.0, beta=1.0):
        """
        Inicializa uma formiga.
        
        :param graph: O objeto Graph onde a formiga vai "viver".
        :param alpha: Influência do feromônio (como no PDF, hardcoded '2').
        :param beta: Influência da heurística (como no PDF, '1').
        """
        self.graph = graph
        self.alpha = alpha
        self.beta = beta
        
        # Começa a clique em um nó aleatório
        start_node = np.random.randint(graph.num_nodes)
        self.clique = [start_node]
        self.clique_size = 1

    def _select_next_node(self):
        """
        Lógica principal: decide qual nó adicionar à clique.
        """
        # 1. Achar candidatos: Nós que NÃO estão na clique
        candidate_nodes = set(range(self.graph.num_nodes)) - set(self.clique)
        if not candidate_nodes:
            return None # Não há mais candidatos

        possible_moves = []
        
        # 2. Filtrar candidatos: Achar quem é conectado a TODOS da clique atual
        for node in candidate_nodes:
            is_fully_connected = True
            for clique_member in self.clique:
                if self.graph.adjacency[node][clique_member] == 0:
                    is_fully_connected = False
                    break
            
            if is_fully_connected:
                possible_moves.append(node)

        # 3. Se não há movimentos possíveis, a clique está completa
        if not possible_moves:
            return None 

        # 4. Calcular probabilidade de escolha 
        probabilities = []
        # ESTE É O LOOP CRÍTICO
        for node in possible_moves: 
            dynamic_heuristic = 0
            
            # (Loop interno para calcular a heurística dinâmica)
            for other_node in possible_moves:
                if node != other_node and self.graph.adjacency[node][other_node] == 1:
                    dynamic_heuristic += 1
            
            # **AQUI É ONDE O CÓDIGO DEVE ESTAR (IDENTADO CORRETAMENTE)**
            # Calcula a influência da heurística e do feromônio para o 'node' atual
            heuristic = (dynamic_heuristic + 1) ** self.beta 
            pheromone = self.graph.pheromones[node] ** self.alpha
            
            # Adiciona a atratividade para este nó na lista
            probabilities.append(pheromone * heuristic)

        # Continua daqui, fora do loop 'for node':
        probabilities = np.array(probabilities, dtype=float)
        
        # Normalizar para que a soma seja 1
        sum_probs = np.sum(probabilities)
        if sum_probs == 0:
            # Se todos os valores forem zero, escolhe aleatoriamente
            probabilities = np.ones_like(probabilities) / len(probabilities)
        else:
            probabilities /= sum_probs
            
        # 5. Escolher o próximo nó com base nas probabilidades
        next_node = np.random.choice(possible_moves, p=probabilities)
        return next_node

    def build_clique(self):
        """
        Continua adicionando nós à clique até não poder mais.
        """
        while True:
            next_node = self._select_next_node()
            if next_node is None:
                break # A formiga "ficou presa", não há mais nós para adicionar
            
            # Adiciona o nó válido à clique
            self.clique.append(next_node)
            self.clique_size += 1