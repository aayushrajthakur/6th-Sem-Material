class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        lastnode = self.head
        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode
    def display(self):
        temp = self.head
        print("The value in the list : ")
        while temp:
            print(temp.data,"-> ",end="")
            temp = temp.next
        print("None")

    def delete(self,key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node  = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    li = LinkedList()
    li.append(10)
    li.append(20)
    li.append(30)
    li.display()
    li.append(40)
    li.append(79)
    li.display()
    li.reverse()
    li.display()