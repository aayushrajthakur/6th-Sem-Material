class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(5)
list1 = Node(10)
list2 = Node(20)
list3 = Node(30)
list4 = Node(40)

head.next = list1
list1.next = list2
list2.next = list3
list3.next = list4