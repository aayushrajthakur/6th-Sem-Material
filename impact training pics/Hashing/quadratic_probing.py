class Quadratic_probing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash(key)
        i = 0
        while self.table[(index + i * i) % self.size] is not None:
            if self.table[(index + i * i) % self.size][0] == key:
                self.table[(index + i * i) % self.size] = (key, value)
                return
            i += 1
            if i == self.size:
                raise Exception('Table is full')
        self.table[(index + i * i) % self.size] = (key, value)

    def search(self, key):
        index = self.hash(key)
        i = 0
        while self.table[(index + i * i) % self.size] is not None:
            if self.table[(index + i * i) % self.size][0] == key:
                return self.table[(index + i * i) % self.size][1]
            i += 1
            if i == self.size:
                break
        return None

    def delete(self, key):
        index = self.hash(key)
        i = 0
        while self.table[(index + i * i) % self.size] is not None:
            if self.table[(index + i * i) % self.size][0] == key:
                self.table[(index + i * i) % self.size] = None
                next_index = (index + (i + 1) * (i + 1)) % self.size
                while self.table[next_index] is not None:
                    rehash_key, rehash_value = self.table[next_index]
                    self.table[next_index] = None
                    self.insert(rehash_key, rehash_value)
                    next_index = (next_index + 1) % self.size
                return
            i += 1
            if i == self.size:
                break

    def display(self):
        for i, j in enumerate(self.table):
            print(i, end=' ')
            if j is not None:
                print('-->', end=' ')
                print(j, end=' ')
            print()

qp = Quadratic_probing(5)
qp.insert(10, 10)
qp.insert(7, 20)
qp.insert(22, 20)

qp.display()
