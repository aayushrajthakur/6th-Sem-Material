import networkx as nx
import heapq
from collections import deque
import matplotlib.pyplot as plt

def dijkstra(graph, start):
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
         
        # Explore neighbors
        for neighbor, weight_dict in graph[current_node].items():
            weight = weight_dict['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
     
    return distances

def ford_fulkerson(graph, source, sink):
    # Create a residual graph
    residual_graph = graph.copy()
    max_flow = 0

    while True:
        # Find an augmenting path using BFS
        path, flow = bfs(residual_graph, source, sink)
        if flow == 0:
            break  # No more augmenting path

        # Update residual capacities of the edges and reverse edges
        max_flow += flow
        for u, v in path:
            residual_graph[u][v]['weight'] -= flow
            if (v, u) not in residual_graph:
                residual_graph.add_edge(v, u, weight=0)
            residual_graph[v][u]['weight'] += flow

    return max_flow

def bfs(residual_graph, source, sink):
    queue = deque([source])
    visited = {source}
    parent = {source: None}
    flow = float('inf')

    while queue:
        current = queue.popleft()

        if current == sink:
            # Reconstruct the path
            path = []
            while parent[current] is not None:
                path.append((parent[current], current))
                current = parent[current]
            return path[::-1], flow

        for neighbor, weight_dict in residual_graph[current].items():
            weight = weight_dict['weight']
            if neighbor not in visited and weight > 0:  # Only consider positive capacity edges
                visited.add(neighbor)
                parent[neighbor] = current
                flow = min(flow, weight)
                queue.append(neighbor)

    return [], 0  # No path found

# Example usage
graph = nx.DiGraph()
graph.add_edge('A', 'B', weight=3)
graph.add_edge('A', 'C', weight=2)
graph.add_edge('B', 'C', weight=1)
graph.add_edge('B', 'D', weight=2)
graph.add_edge('C', 'D', weight=4)

source = 'A'
sink = 'D'
max_flow = ford_fulkerson(graph, source, sink)
print("The maximum possible flow is:", max_flow)

# Visualization of the flow network
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=15, font_weight="bold")
edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')
