class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._balanced_insert(self.root, data)

    def _balanced_insert(self,current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._balanced_insert(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._balanced_insert(current_node.right, data)

    def inorder_Traversal(self,node):
        if node:
            self.inorder_Traversal(node.left)
            print(node.data,end=" ")
            self.inorder_Traversal(node.right)

    def preOrder_traversal(self,node):
        if node:
            print(node.data, end=" ")
            self.preOrder_traversal(node.left)
            self.preOrder_traversal(node.right)
    def postOrder_Traversal(self,node):
        if node:
            self.postOrder_Traversal(node.left)
            self.postOrder_Traversal(node.right)
            print(node.data, end=" ")

binarytree = BinaryTree()
li = [6,3,5,9,12,65,34,17,94]
for i in range(len(li)):
    binarytree.insert(li[i])
print("The inorder traversal : ")
binarytree.inorder_Traversal(binarytree.root)


