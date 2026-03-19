class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k  # массив фиксированного размера
        self.k = k
        self.front = 0        # начало
        self.rear = -1        # конец
        self.count = 0        # количество элементов

    def enQueue(self, value: int) -> bool:
        # если очередь полная
        if self.isFull():
            return False
        
        # двигаем указатель по кругу
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        # если очередь пустая
        if self.isEmpty():
            return False
        
        # двигаем начало по кругу
        self.front = (self.front + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.k