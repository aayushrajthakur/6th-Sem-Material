import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(str(node.data))
            self.inorder_traversal(node.right, result)
        return result

    def find_lca(self, root, n1, n2):
        if root is None:
            return None

        if root.data > n1 and root.data > n2:
            return self.find_lca(root.left, n1, n2)
        if root.data < n1 and root.data < n2:
            return self.find_lca(root.right, n1, n2)

        return root

def insert_data():
    data = int(entry.get())
    tree.insert(data)
    entry.delete(0, tk.END)
    messagebox.showinfo("Information", f"Inserted {data}")

def display_tree():
    result = tree.inorder_traversal(tree.root, [])
    messagebox.showinfo("Inorder Traversal", " -> ".join(result))

def find_lca():
    n1 = int(simpledialog.askstring("Input", "Enter the first node value:"))
    n2 = int(simpledialog.askstring("Input", "Enter the second node value:"))
    lca_node = tree.find_lca(tree.root, n1, n2)
    if lca_node:
        messagebox.showinfo("LCA", f"The Lowest Common Ancestor of {n1} and {n2} is {lca_node.data}")
    else:
        messagebox.showinfo("LCA", "No common ancestor found")

def visualize_tree(canvas, node, x, y, spacing):
    if node:
        canvas.create_text(x, y, text=str(node.data), font=("Helvetica", 12), tags="tree")
        if node.left:
            canvas.create_line(x, y, x - spacing, y + 40, arrow=tk.LAST, tags="tree")
            visualize_tree(canvas, node.left, x - spacing, y + 40, spacing // 2)
        if node.right:
            canvas.create_line(x, y, x + spacing, y + 40, arrow=tk.LAST, tags="tree")
            visualize_tree(canvas, node.right, x + spacing, y + 40, spacing // 2)

def update_canvas():
    canvas.delete("tree")
    visualize_tree(canvas, tree.root, 300, 20, 100)

# Creating the main window
root = tk.Tk()
root.title("Binary Tree GUI")

tree = BinaryTree()

# Creating the GUI elements
label = tk.Label(root, text="Enter data to insert:")
label.pack()

entry = tk.Entry(root)
entry.pack()

insert_button = tk.Button(root, text="Insert", command=lambda: [insert_data(), update_canvas()])
insert_button.pack()

display_button = tk.Button(root, text="Display Inorder Traversal", command=display_tree)
display_button.pack()

lca_button = tk.Button(root, text="Find LCA", command=find_lca)
lca_button.pack()

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

# Run the GUI event loop
root.mainloop()
