import networkx as nx
import heapq
from collections import deque
import matplotlib.pyplot as plt



def ford_fulkerson(graph, source, sink):
    residual_graph = graph.copy()
    max_flow = 0

    while True:
        path, flow = bfs(residual_graph, source, sink)
        if flow == 0:
            break 

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
            path = []
            while parent[current] is not None:
                path.append((parent[current], current))
                current = parent[current]
            return path[::-1], flow

        for neighbor, weight_dict in residual_graph[current].items():
            weight = weight_dict['weight']
            if neighbor not in visited and weight > 0:
                visited.add(neighbor)
                parent[neighbor] = current
                flow = min(flow, weight)
                queue.append(neighbor)

    return [], 0

graph = nx.DiGraph()
graph.add_edge('A', 'B', weight=5)
graph.add_edge('B', 'C', weight=3)
graph.add_edge('B', 'G', weight=4)
graph.add_edge('C', 'D', weight=4)
graph.add_edge('D', 'E', weight=6)
graph.add_edge('D', 'F', weight=7)
graph.add_edge('E', 'K', weight=2)
graph.add_edge('G', 'F', weight=8)
graph.add_edge('F', 'K', weight=4)
graph.add_edge('G', 'H', weight=1)
graph.add_edge('H', 'I', weight=3)
graph.add_edge('I', 'J', weight=6)
graph.add_edge('J', 'K', weight=5)


source = 'B'
sink = 'I'
max_flow = ford_fulkerson(graph, source, sink)
print("The maximum possible flow is:", max_flow)

pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=15, font_weight="bold")
edge_labels = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')
plt.title("Flow Network")
plt.axis("off")
plt.show()
