import heapq

def dijkstra(graph, start):
    distance = {node: float('inf') for node in graph}
    distance[start] = 0

    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distance[current_node]:
            continue

        for neighbor, properties in graph[current_node].items():
            weight = properties['weight']
            distance_through_current = current_distance + weight

            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                heapq.heappush(pq, (distance_through_current, neighbor))

    return distance

graph = {
    'A': {'B': {'weight': 2}, 'C': {'weight': 1}},
    'B': {'A': {'weight': 2}, 'C': {'weight': 4}, 'D': {'weight': 3}},
    'C': {'A': {'weight': 1}, 'B': {'weight': 4}, 'D': {'weight': 5}},
    'D': {'B': {'weight': 3}, 'C': {'weight': 5}}
}
start_node = 'A'
distances = dijkstra(graph, start_node)
print(distances)
