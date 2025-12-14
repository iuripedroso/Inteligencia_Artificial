## Projetos de Inteligência Artificial

Este repositório contém projetos acadêmicos desenvolvidos em Python durante a graduação, envolvendo **Algoritmos Genéticos**, **Colônia de Formigas**, **Redes Neurais MLP** e **Algoritmos de Rotas**.

## Estrutura do Repositório

- **Algoritmo Genético**  
  Implementações de algoritmos genéticos para diferentes problemas, com análise de resultados e visualização de desempenho.

- **Colônia de Formigas**  
  Implementações do algoritmo de colônia de formigas aplicadas ao problema do clique, com scripts em Python e arquivos de configuração.

- **Redes Neurais (MLP) - Predição da Qualidade de Vinhos**  
  Rede neural multicamadas implementada para prever a qualidade de vinhos utilizando backpropagation. Contém:
  - Dados (`.csv`) de vinhos brancos e tintos  
  - Scripts de treino e teste  
  - Resultados gráficos (`.png`)  
  - Código modular em `src/` para `data_loader`, `model`, `train` e `utils`

- **Algoritmo de Rotas**  
  Projetos relacionados a cálculo de rotas, incluindo documentação e código-fonte.


## Detalhes da Implementação

### Algoritmo Genético
- Manipulação de **cromossomos**, operadores genéticos (crossover, mutação), seleção e avaliação de fitness.
- Scripts para análise de resultados (`analise_resultados.py`).

### Colônia de Formigas
- Implementação do **ACO (Ant Colony Optimization)** para o problema do clique.
- Classes em Python para **grafo, formigas e execução do algoritmo**.
- Armazenamento de resultados em `highscores.json`.

### Redes Neurais MLP
- Treino supervisionado utilizando **backpropagation**.
- Consumo de datasets `.csv`, pré-processamento e modelagem.
- Visualização de curvas de perda (`loss_curve.png`) e resultados de testes.

### Algoritmo de Rotas
- Cálculo e otimização de rotas.
- Código organizado em pastas específicas para cada implementação.

## Tecnologias Utilizadas

- Python 3.x  
- Bibliotecas: `numpy`, `pandas`, `matplotlib`  
- PIL para manipulação de imagens  
- Estruturas de dados personalizadas para algoritmos
