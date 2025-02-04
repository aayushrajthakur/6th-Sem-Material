class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.stack = []
    
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            self.stack.append(data)
        else:
            self._insert_recursively(self.root,data)
    
    def _insert_recursively(self,node,data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursively(node.left,data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursively(node.right, data)

    def inorder_Traversal(self,node):
        if node:
            self.inorder_Traversal(node.left)
            print(node.data," ->",end=" ")
            self.inorder_Traversal(node.right)
        
if __name__ == "__main__":
    bi = BinaryTree()
    condition =  True
    print("Program implementation for Lowest Common Ancestors : ")
    while condition:
        print("Select one of the options : ")
        print("1. Press 1 to insert the data")
        print("2. Press 2 to insert the delete")
        print("3. Press 3 to display the result")
        print("4. Press 4 to find the Lowest Common Ancestor")
        print("5. Press 5 to exit the program.")
        option = int(input("Enter the option : "))
        if option == 1:
            data = int(input("Enter the data : "))
            bi.insert(data)
        elif option == 2:
            data = int(input("Enter the data to be delete : "))
            bi.delete(data)
        elif option == 3:
            bi.display()
        elif option == 4:
            bi.lca()
        elif option ==  5:
            print("You are exiting the program.")
            condition =  False
        else:
            print("Please, input the valid option. ")

        
