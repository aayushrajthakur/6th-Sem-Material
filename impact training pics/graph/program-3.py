import networkx as nx
import heapq
import matplotlib.pyplot as plt

def dijkstra(graph, start, traps):
    # Initialize distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
       
    # Initialize priority queue
    pq = [(0, start)]
    while pq:
        current_distance, current_node = heapq.heappop(pq)
         
        # If we already found a shorter path, skip
        if current_distance > distances[current_node]:
            continue

        # Skip if the current node is a trap
        if current_node in traps:
            continue
         
        # Explore neighbors
        for neighbor, weight_dict in graph[current_node].items():
            weight = weight_dict['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
     
    return distances

def find_shortest_safe_path(graph, start, treasure, traps):
    distances = dijkstra(graph, start, traps)
    if distances[treasure] == float('inf'):
        return "No safe path exists."
    
    # Reconstruct the path (not implemented in this version)
    return distances[treasure]

# Example graph
graph = {
    'A': {'B': {'weight': 2}, 'C': {'weight': 1}},
    'B': {'A': {'weight': 2}, 'C': {'weight': 4}, 'D': {'weight': 3}},
    'C': {'A': {'weight': 1}, 'B': {'weight': 4}, 'D': {'weight': 5}},
    'D': {'B': {'weight': 3}, 'C': {'weight': 5}}
}
start_node = 'C'
treasure_node = 'A'
trap_nodes = ['B']  # Example trap nodes
shortest_safe_path = find_shortest_safe_path(graph, start_node, treasure_node, trap_nodes)

print("Shortest safe path distance:", shortest_safe_path)

# Visualization (optional)
G = nx.DiGraph(graph)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=False, node_size=1500, node_color="skyblue", font_size=15, font_weight="bold")
edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Graph Visualization")
plt.axis("off")
plt.show()
