import networkx as nx
import matplotlib.pyplot as plt
from graph import create_kiev_metro_graph

G = create_kiev_metro_graph()

# Додаємо ваги до ребер (припустимо, що всі відстані між станціями однакові, наприклад, 1)
for edge in G.edges():
    G.edges[edge]['weight'] = 1

def dijkstra_path(graph, start, goal):
    return nx.dijkstra_path(graph, start, goal), nx.dijkstra_path_length(graph, start, goal)

# Визначимо стартову і кінцеву станції
start_station = "Академмістечко"
goal_station = "Лісова"

# Знайдемо найкоротший шлях за допомогою алгоритму Дейкстри
dijkstra_result, dijkstra_length = dijkstra_path(G, start_station, goal_station)

print("Дейкстра шлях:", " -> ".join(dijkstra_result))
print("Довжина шляху (вага):", dijkstra_length)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

# Виділимо найкоротший шлях
if dijkstra_result:
    dijkstra_edges = [(dijkstra_result[i], dijkstra_result[i + 1]) for i in range(len(dijkstra_result) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=dijkstra_edges, edge_color="green", width=2)

plt.title("Найкоротший шлях за допомогою алгоритму Дейкстри у Київському метрополітені")
plt.show()
