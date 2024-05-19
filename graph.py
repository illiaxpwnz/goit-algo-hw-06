import networkx as nx
import matplotlib.pyplot as plt

def create_kiev_metro_graph():
    G = nx.Graph()

    # Додаємо вузли (станції метро)
    stations = {
        "M1": ["Академмістечко", "Житомирська", "Святошин", "Нивки", "Берестейська", "Шулявська", "Політехнічний інститут", "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна", "Дарниця", "Чернігівська", "Лісова"],
        "M2": ["Героїв Дніпра", "Мінська", "Оболонь", "Почайна", "Тараса Шевченка", "Контрактова площа", "Поштова площа", "Майдан Незалежності", "Площа Льва Толстого", "Олімпійська", "Палац 'Україна'", "Либідська", "Деміївська", "Голосіївська", "Васильківська", "Виставковий центр", "Іподром", "Теремки"],
        "M3": ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті Ворота", "Палац спорту", "Кловська", "Печерська", "Дружби народів", "Видубичі", "Славутич", "Осокорки", "Позняки", "Харківська", "Вирлиця", "Бориспільська", "Червоний Хутір"]
    }

    for line, stations_list in stations.items():
        G.add_nodes_from(stations_list)

    # Додаємо ребра
    edges = []
    for stations_list in stations.values():
        edges.extend([(stations_list[i], stations_list[i + 1]) for i in range(len(stations_list) - 1)])
    G.add_edges_from(edges)

    # Додаємо пересадки
    transfers = [
        ("Театральна", "Золоті Ворота"),  # Пересадка M1-M3
        ("Хрещатик", "Майдан Незалежності"),  # Пересадка M1-M2
        ("Палац спорту", "Площа Льва Толстого")  # Пересадка M3-M2
    ]
    G.add_edges_from(transfers)

    return G

if __name__ == "__main__":
    G = create_kiev_metro_graph()

    # Візуалізація графу
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold", edge_color="gray")
    plt.title("Транспортна мережа Київського метрополітену")
    plt.show()

    # Аналіз основних характеристик графу
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degree = dict(G.degree())

    print(f"Кількість вершин: {num_nodes}")
    print(f"Кількість ребер: {num_edges}")
    print("Ступінь вершин (перші 10):")
    for node, deg in list(degree.items())[:10]:
        print(f"Вершина {node}: ступінь {deg}")
