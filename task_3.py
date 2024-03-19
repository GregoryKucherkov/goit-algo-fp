import heapq
import networkx as nx

# dijkstra algorithm using heap
def dijkstra(graph, start):
    shortest_dist = {vertex: float('infinity') for vertex in graph}
    shortest_dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_dist[neighbor]:
                shortest_dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_dist


# A graph representation a modified portion of the New York City subway system
G = nx.Graph()
edges_with_weights =  [
    ("WHitehall", "Rector", {'weight': 2}),
    ("WHitehall", "Bowling", {'weight': 1}),
    ("WHitehall", "Cortland", {'weight': 2}),
    ("WHitehall", "City_hall", {'weight': 2}),
    ("Rector", "Rector_green", {'weight': 1}),
    ("Rector", "Cortland", {'weight': 2}),
    ("Cortland", "Cortland_green", {'weight': 1}),
    ("Bowling", "Rector_green", {'weight': 1}),
    ("Rector_green", "Wall_st", {'weight': 1}),
    ("Wall_st", "Cortland_green", {'weight': 1}),
    ("Cortland", "City_hall", {'weight': 2}),
    ("Cortland_green", "Chambers", {'weight': 2}),
    ("City_hall", "Canal", {'weight': 2}),
    ("Bowling", "Borough", {'weight': 4})
]

G.add_edges_from(edges_with_weights)


if __name__ == "__main__":
    result = dijkstra(G, "WHitehall")
    print(f'The shortest ways from the starting point to all others: {result}')

