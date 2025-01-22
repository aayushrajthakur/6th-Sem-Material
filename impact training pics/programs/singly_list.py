class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class SingleLinkedList:
  def __init__(self):
    self.head=None
    
  def isEmpty(self):
    return self.head is None
    
  def append(self,data):
    new_node=Node(data)
    if self.isEmpty():
      self.head=new_node
      return 
    else:
      current_node=self.head
      while current_node.next:
        current_node=current_node.next
      current_node=new_node
      
  def prepand(self,data):
    new_node=Node(data)
    new_node.next=self.head
    self.head=new_node
    
  def InsertAfterPerticularNode(self,prev_data,data):
    current=self.head
    while current and current.data !=prev_data:
      current=current.next
      if not current:
        print(f"Node with the data {prev_data} not found")
        return 
      else:
        new_node=Node(data)
        new_node.next=current.next
        current.next=new_node
  def delete(self,key):
    current_node=self.head
    if current_node and current_node.data==key:
      self.head=current_node.next
      current_node=None
      return
    prev=None
    while current_node and current_node.data!=key:
      prev=current_node
      current_node=current_node.next
      if not current_node:
        print(f"Node with the data {key} not found")
        return 
      prev.next=current_node.next
      current_node=None
  def print_Linked_List(self):
    current_node=self.head
    while current_node:
      print(current_node.data,end="->")
      current_node=current_node.next
    print("None")
    
s1=SingleLinkedList()
s1.append(10)
s1.append(20)
s1.append(30)
print("Initial linked list")
s1.print_Linked_List()