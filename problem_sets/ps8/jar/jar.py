class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * str("🍪")

    def deposit(self, n):
        if self.size <= self.capacity - n:
            self.size += n
            return self.size
        else:
            raise ValueError("Not enough capacity for added cookies")

    def withdraw(self, n):
        if self.size >= n:
            self.size -= n
        else:
            raise ValueError("Not enough cookies in jar")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        capacity = int(capacity)
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity must be a positive integer")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: int):
        if 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError
