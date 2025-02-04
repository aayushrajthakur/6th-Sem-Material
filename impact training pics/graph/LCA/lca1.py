import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# TreeNode class to represent a node in the binary tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to find the Lowest Common Ancestor
def lowest_common_ancestor(root, p, q):
    if not root:
        return None
    if root.val == p or root.val == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

# Function to build a graph from the binary tree
def build_graph(root, graph=None):
    if graph is None:
        graph = nx.Graph()
    if root:
        if root.left:
            graph.add_edge(root.val, root.left.val)
            build_graph(root.left, graph)
        if root.right:
            graph.add_edge(root.val, root.right.val)
            build_graph(root.right, graph)
    return graph

# Function to visualize the binary tree and highlight the LCA node
def visualize_tree_with_lca(root, p, q, canvas):
    # Find the LCA
    lca_node = lowest_common_ancestor(root, p, q)
    
    # Build the graph
    graph = build_graph(root)
    
    # Get positions for the nodes in the graph
    pos = nx.spring_layout(graph)
    
    # Clear the previous plot
    canvas.figure.clear()
    
    # Draw the graph
    ax = canvas.figure.add_subplot(111)
    nx.draw(graph, pos, ax=ax, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold')
    
    # Highlight the LCA node
    if lca_node:
        nx.draw_networkx_nodes(graph, pos, nodelist=[lca_node.val], node_color='red', node_size=2000)
    
    ax.set_title(f"Lowest Common Ancestor of {p} and {q} is {lca_node.val if lca_node else 'None'}")
    canvas.draw()

# Function to handle the GUI input and visualization
def on_submit():
    try:
        # Get user inputs
        root_val = int(root_entry.get())
        left_val = int(left_entry.get()) if left_entry.get() else None
        right_val = int(right_entry.get()) if right_entry.get() else None
        p = int(p_entry.get())
        q = int(q_entry.get())
        
        # Build the binary tree
        root = TreeNode(root_val)
        if left_val is not None:
            root.left = TreeNode(left_val)
        if right_val is not None:
            root.right = TreeNode(right_val)
        
        # Visualize the tree and highlight the LCA
        visualize_tree_with_lca(root, p, q, canvas)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values.")

# Create the main GUI window
root_window = tk.Tk()
root_window.title("Lowest Common Ancestor Visualizer")

# Create input fields
tk.Label(root_window, text="Root Node:").grid(row=0, column=0, padx=10, pady=10)
root_entry = tk.Entry(root_window)
root_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root_window, text="Left Node:").grid(row=1, column=0, padx=10, pady=10)
left_entry = tk.Entry(root_window)
left_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root_window, text="Right Node:").grid(row=2, column=0, padx=10, pady=10)
right_entry = tk.Entry(root_window)
right_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Label(root_window, text="Node p:").grid(row=3, column=0, padx=10, pady=10)
p_entry = tk.Entry(root_window)
p_entry.grid(row=3, column=1, padx=10, pady=10)

tk.Label(root_window, text="Node q:").grid(row=4, column=0, padx=10, pady=10)
q_entry = tk.Entry(root_window)
q_entry.grid(row=4, column=1, padx=10, pady=10)

# Submit button
submit_button = tk.Button(root_window, text="Find LCA", command=on_submit)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

# Create a canvas for matplotlib figure
fig = plt.figure(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=root_window)
canvas.get_tk_widget().grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI
root_window.mainloop()