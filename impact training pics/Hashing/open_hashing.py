class HashTable:
    def __init__(self,size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append((key, value))

    def search(self,key):
        index = self.hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    def delete(self,key):
        index = self.hash(key)
        for i,pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return
        raise KeyError('Key not found')
    
    def display(self):
        for i,j in enumerate(self.table):
            print(i,end = ' ')
            for k in j:
                print('-->',end = ' ')
                print(k,end = ' ')
            print()

ht = HashTable(5)
ht.insert('a')
ht.insert('b')
ht.insert('c')
ht.insert('d')
ht.insert('e')
