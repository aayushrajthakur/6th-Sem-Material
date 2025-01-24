class queue:
  def __init__(self,data):
    self.data = data
    self.prev = None
    self.next = None


class queueImplementation:
  def __init__(self):
    self.front = self.rare = None


  def append(self,data):
    new_node = queue(data)
    if self.front == None and self.rare == None:
      self.front = self.rare = new_node
      return
    else :
      new_node.prev = self.front
      self.front.next = new_node
      self.front = new_node
      return
    
  def pop(self):
    if self.rare is None:
        return
    else:
        temp = self.rare
        self.rare = self.rare.prev
        if self.rare is None:
            self.front = None
        del temp
        return

  def display(self):
    if self.front == None and self.rare == None:
        print("The queue is empty.")
        return
    print("The elements are : ",end=" ")
    temp = self.front
    while(temp):
        print(temp.data,"<-> ",end="")
        temp = temp.prev
    print("None")

q1 = queueImplementation()
q1.append(10)
q1.append(20)
q1.append(30)
q1.display()

q1.pop
q1.display()









      
        


  