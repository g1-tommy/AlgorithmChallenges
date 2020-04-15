# 11866 요세푸스 문제 0
"""
풀이: Circular Queue 이용
"""
class CircularQueue():
    def __init__(self, size=10):
        self.maxSize = size
        self.size = 0
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.maxSize
    
    def enqueue(self, data):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.maxSize
            self.queue[self.rear] = data
            self.size += 1
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.maxSize
            self.size -= 1
            return self.queue[self.front]
    
if __name__ == "__main__":
    N, K = map(int, input().split())
    cirQueue = CircularQueue(N)
    sequence = list()
    for i in range(1, N + 1):
        cirQueue.enqueue(i)
    
    while not cirQueue.isEmpty():
        for i in range(K - 1):
            cirQueue.enqueue(cirQueue.dequeue())
        sequence.append(cirQueue.dequeue())
    
    sequence = ", ".join(map(str, sequence))
    print(f"<{sequence}>")