import matplotlib.pyplot as plt
import networkx as nx

# Перенесення графу з першого завдання
def create_kiev_metro_graph():
    G = {
        "Академмістечко": {"Житомирська": 1},
        "Житомирська": {"Академмістечко": 1, "Святошин": 1},
        "Святошин": {"Житомирська": 1, "Нивки": 1},
        "Нивки": {"Святошин": 1, "Берестейська": 1},
        "Берестейська": {"Нивки": 1, "Шулявська": 1},
        "Шулявська": {"Берестейська": 1, "Політехнічний інститут": 1},
        "Політехнічний інститут": {"Шулявська": 1, "Вокзальна": 1},
        "Вокзальна": {"Політехнічний інститут": 1, "Університет": 1},
        "Університет": {"Вокзальна": 1, "Театральна": 1},
        "Театральна": {"Університет": 1, "Хрещатик": 1},
        "Хрещатик": {"Театральна": 1, "Арсенальна": 1},
        "Арсенальна": {"Хрещатик": 1, "Дніпро": 1},
        "Дніпро": {"Арсенальна": 1, "Гідропарк": 1},
        "Гідропарк": {"Дніпро": 1, "Лівобережна": 1},
        "Лівобережна": {"Гідропарк": 1, "Дарниця": 1},
        "Дарниця": {"Лівобережна": 1, "Чернігівська": 1},
        "Чернігівська": {"Дарниця": 1, "Лісова": 1},
        "Лісова": {"Чернігівська": 1}
    }
    return G

def dijkstra(graph, start, goal):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex

        unvisited.remove(current_vertex)

    path = []
    current_node = goal
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    
    if distances[goal] == float('infinity'):
        return "Route Not Possible", float('infinity')
    return path, distances[goal]

G = create_kiev_metro_graph()

# Стартова та кінцеві станції
start_station = "Академмістечко"
goal_station = "Хрещатик"

# найкоротший шлях
dijkstra_result, dijkstra_length = dijkstra(G, start_station, goal_station)

print("Дейкстра шлях:", " -> ".join(dijkstra_result))
print("Довжина шляху (вага):", dijkstra_length)

# Візуалізація
G_nx = nx.Graph()
for node, edges in G.items():
    for neighbor, weight in edges.items():
        G_nx.add_edge(node, neighbor, weight=weight)

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G_nx)
nx.draw(G_nx, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

if dijkstra_result:
    dijkstra_edges = [(dijkstra_result[i], dijkstra_result[i + 1]) for i in range(len(dijkstra_result) - 1)]
    nx.draw_networkx_edges(G_nx, pos, edgelist=dijkstra_edges, edge_color="green", width=2)

plt.title("Найкоротший шлях за допомогою алгоритму Дейкстри у Київському метрополітені")
plt.show()
