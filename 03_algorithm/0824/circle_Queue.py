class Queue:

    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.rear = 0
        self.front = 0

    def enQueue(self, item):
        if self.isFull():
            print('is Full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item

    def deQueue(self):
        self.front = (self.front + 1) % self.size
        return self.items[self.front]

    def isFull(self):
        return self.front == (self.rear + 1) % self.size

q = Queue(5)
print(q.items)

q.enQueue('A')
q.enQueue('B')
print(q.items)

print('='*30)
print(q.items)

q.enQueue('C')
q.enQueue('D')
print('='*30)
print(q.items)

q.enQueue('E')
print('='*30)
print(q.items)

print('='*30)
print(q.rear, q.front)
