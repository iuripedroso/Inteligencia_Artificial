# main.py
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx # Biblioteca para desenhar grafos

from graph_clique import Graph
from aco_clique import ACO

def generate_random_graph(num_nodes, density=0.5):
    """
    Cria uma matriz de adjacência aleatória para um grafo não-direcionado.
    :param num_nodes: Número de nós
    :param density: Probabilidade de existir uma aresta entre dois nós
    """
    adj_matrix = np.zeros((num_nodes, num_nodes))
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes): # Só preenche o triângulo superior
            if np.random.rand() < density:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1 # Grafo não-direcionado
    return adj_matrix

def plot_clique_solution(adjacency_matrix, best_clique):
    """
    Usa NetworkX para desenhar o grafo em um layout circular
    e destacar a clique encontrada.
    """
    G = nx.from_numpy_array(adjacency_matrix)
    
    plt.figure(figsize=(12, 10)) # Aumentar um pouco a figura para o layout circular

    # --- 1. Calcular Posições em um Layout Circular ---
    # Isso distribuirá todos os nós em um círculo
    pos = nx.circular_layout(G) 
    
    # Você também pode tentar:
    # pos = nx.shell_layout(G) # Níveis concêntricos, pode ser interessante para cliques internas
    # pos = nx.spectral_layout(G) # Bom para separar componentes, mas talvez menos 'organizado' visualmente

    # --- 2. Desenhar todos os nós ---
    # Nós que NÃO são da clique (em azul claro)
    non_clique_nodes = [n for n in G.nodes() if n not in best_clique]
    nx.draw_networkx_nodes(G, pos, nodelist=non_clique_nodes, node_color='lightblue', node_size=600)
    
    # Nós que SÃO da clique (em vermelho)
    if best_clique:
        nx.draw_networkx_nodes(G, pos, nodelist=best_clique, node_color='red', node_size=800) # Ligeiramente maiores

    # --- 3. Desenhar todas as arestas ---
    # Arestas que NÃO são da clique (em cinza, finas)
    # Primeiro, desenhamos todas as arestas com a cor padrão
    nx.draw_networkx_edges(G, pos, edge_color='gray', alpha=0.3, width=1.0) 
    
    # Arestas DENTRO da clique (vermelhas, grossas)
    if best_clique:
        clique_subgraph = G.subgraph(best_clique)
        nx.draw_networkx_edges(clique_subgraph, pos, edge_color='red', width=3.0, alpha=0.9)
    
    # --- 4. Desenhar os labels dos nós ---
    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
    
    plt.title(f"Solução Final: Maior Clique Encontrada (Tamanho: {len(best_clique)}) - Layout Circular")
    plt.axis('off') # Remove os eixos
    plt.show()

def plot_size_over_iterations(best_size_history):
    """
    Plota como o tamanho da clique melhorou (similar ao PDF, source 116)
    """
    plt.figure(figsize=(12, 6))
    plt.plot(best_size_history, color='green', linewidth=2)
    plt.title("Tamanho da Maior Clique por Iteração")
    plt.xlabel("Iteração")
    plt.ylabel("Tamanho da Clique")
    plt.grid(True)
    plt.show()


# --- Bloco de Execução Principal ---
if __name__ == "__main__":
    
    # --- Parâmetros ---
    NUM_NODES = 20       
    GRAPH_DENSITY = 0.6
    NUM_ANTS = 10       
    NUM_ITERATIONS = 30  
    
    # --- 1. Criar o Grafo ---
    adj_matrix = generate_random_graph(NUM_NODES, GRAPH_DENSITY)
    graph = Graph(adj_matrix)
    
    # --- 2. Configurar e Rodar o ACO ---
    aco = ACO(graph, num_ants=NUM_ANTS, num_iterations=NUM_ITERATIONS)
    best_clique, best_size = aco.run()
    
    # --- 3. Imprimir e Plotar Resultados ---
    print(f"\n--- Resultados ---")
    print(f"Melhor clique encontrada: {best_clique}")
    print(f"Tamanho: {best_size}")
    
    # Plotar o grafo da solução (como no PDF, source 124)
    plot_clique_solution(adj_matrix, best_clique)
    
    # Plotar a convergência (como no PDF, source 125)
    plot_size_over_iterations(aco.best_size_history)