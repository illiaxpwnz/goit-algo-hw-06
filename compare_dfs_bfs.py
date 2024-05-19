def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))
    return None

def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                return path + [next]
            else:
                queue.append((next, path + [next]))
    return None

# Визначимо стартову і кінцеву станції
start_station = "Академмістечко"
goal_station = "Лісова"

# Знайдемо шляхи за допомогою DFS та BFS
dfs_result = dfs_path(G, start_station, goal_station)
bfs_result = bfs_path(G, start_station, goal_station)

print("DFS шлях:", " -> ".join(dfs_result))
print("BFS шлях:", " -> ".join(bfs_result))

# Візуалізація графу з виділенням шляхів
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")

if dfs_result:
    dfs_edges = [(dfs_result[i], dfs_result[i + 1]) for i in range(len(dfs_result) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color="red", width=2)

if bfs_result:
    bfs_edges = [(bfs_result[i], bfs_result[i + 1]) for i in range(len(bfs_result) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color="blue", width=2, style="dashed")

plt.title("Шляхи DFS та BFS у Київському метрополітені")
plt.show()
