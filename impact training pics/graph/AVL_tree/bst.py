import networkx as nx
import matplotlib.pyplot as plt

class Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        if self.root is None:
            self.root = Tree(data)
            return
        else:
            self._insert_recursively(self.root,data)

    def _insert_recursively(self,node,data):
            if data < node.data:
                if node.left is None:
                    node.left= Tree(data)
                else:
                    self._insert_recursively(node.left,data)
            else:
                if node.right is None:
                    node.right = Tree(data)
                    return
                else:
                    self._insert_recursively(node.right,data)
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None or node.data == data:
            return node

        if data < node.data:
            return self._search(node.left, data)
        else:
            return self._search(node.right, data)
    
    def inorderTraversal(self):
        return self._inorderTraversal(self.root)

    def _inorderTraversal(self,node):
        if node:
            self._inorderTraversal(node.left)
            print(node.data,end=" ")
            self._inorderTraversal(node.right)
    
    def preorderTraversal(self):
        return self._preorderTraversal(self.root)

    def _preorderTraversal(self,node):
        if node:
            print(node.data,end=" ")
            self._preorderTraversal(node.left)
            self._preorderTraversal(node.right)
    
    def postorderTraversal(self):
        return self._postorderTraversal(self.root)

    def _postorderTraversal(self,node):
        if node:
            self._postorderTraversal(node.left)
            self._postorderTraversal(node.right)
            print(node.data,end=" ")
    
    def add_edges(self, G, node, pos, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.data, pos=(x, y))
            if node.left:
                G.add_edge(node.data, node.left.data)
                l = x - 1 / layer
                self.add_edges(G, node.left, pos, x=l, y=y-1, layer=layer+1)
            if node.right:
                G.add_edge(node.data, node.right.data)
                r = x + 1 / layer
                self.add_edges(G, node.right, pos, x=r, y=y-1, layer=layer+1)

    def plot_tree(self):
        G = nx.DiGraph()
        pos = {}
        self.add_edges(G, self.root, pos)
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True, arrows=False)
        plt.show()
        plt.close()  

if __name__ == "__main__":
    bst = BST()
    cond = True
    print("Binary Search Tree")
    while(cond):
        print("1. Press 1 to insert the data individually.")
        print("2. Press 2 to insert data in list.")
        print("3. Press 3 to search.")
        print("4. Press 4 to inorder  Traversal.")
        print("5. Press 5 to preorder Traversal.")
        print("6. Press 6 to postorder Traversal.")
        print("7. Press 7 to plot the graph.")
        opt = int(input("Please, select an option : "))
        if opt == 1:
            data = int(input("Enter the data : "))
            bst.insert(data)
    
        elif opt == 2:
            numbers = input("Enter the numbers : ")
            keys = list(map(int, numbers.split()))
            for key in keys:
                bst.insert(key)
        
        elif opt == 3:
            key = int(input("Enter the key to be search : "))
            node = bst.search(key)
            if node:
                print("Data found..")
            else:
                print("Data not found..")
        
        elif opt == 4:
            print("Inorder Traversal : ",end=" ")
            bst.inorderTraversal()
            print()
        elif opt == 5:
            print("Preorder Traversal : ",end=" ")
            bst.preorderTraversal()
            print()
        elif opt == 6:
            print("Postorder Traversal : ",end=" ")
            bst.postorderTraversal()
            print()
        elif opt == 7:
            bst.plot_tree()
        

        
