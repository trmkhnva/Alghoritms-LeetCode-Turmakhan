class MyQueue:

    def __init__(self):
        self.s1 = []  # стек для добавления
        self.s2 = []  # стек для извлечения

    def push(self, x: int) -> None:
        # просто кладем в первый стек
        self.s1.append(x)

    def pop(self) -> int:
        # если второй стек пуст, переносим элементы
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2