class Jar:
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("capacity is not a non-negative int")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("size exceeds capacity")
        self._size = size

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("capacity is not a non-negative int")
        self._size = 0
        self._capacity = capacity

    def __str__(self):
        return f'{"🍪" * self.size}'

    def deposit(self, n):
        if (self.size + n) > self.capacity:
            raise ValueError("deposit exceeds capacity")
        self.size = self.size + n
        
    def withdraw(self, n):
        if n > self.size:
            raise ValueError("withdraw exceeds size")
        self.size = self.size - n





