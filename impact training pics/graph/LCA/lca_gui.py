import tkinter as tk
import networkx as nx

def lca(graph, node1, node2):
    # Function to find the path from the root to a given node
    def find_path(graph, start, path):
        if start not in graph:
            return None
        path.append(start)
        if start == node1 or start == node2:
            return path
        for neighbor in graph[start]:
            result = find_path(graph, neighbor, path.copy())
            if result:
                return result
        return None

    # Find paths from the root to both nodes
    path1 = find_path(graph, 'A', [])
    path2 = find_path(graph, 'A', [])

    # Find the last common node in both paths
    lca_node = None
    for u, v in zip(path1, path2):
        if u == v:
            lca_node = u
        else:
            break
    return lca_node

def calculate_lca():
    node1 = entry_node1.get()
    node2 = entry_node2.get()
    ancestor = lca(graph, node1, node2)
    result_label.config(text=f"LCA of {node1} and {node2} is: {ancestor}")

# Create a directed graph
graph = nx.DiGraph()
graph.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('B', 'E'),
    ('C', 'F'),
    ('C', 'G')
])

# Set up the GUI
root = tk.Tk()
root.title("Lowest Common Ancestor Finder")

tk.Label(root, text="Node 1:").grid(row=0, column=0)
entry_node1 = tk.Entry(root)
entry_node1.grid(row=0, column=1)

tk.Label(root, text="Node 2:").grid(row=1, column=0)
entry_node2 = tk.Entry(root)
entry_node2.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate LCA", command=calculate_lca)
calculate_button.grid(row=2, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

root.mainloop()
