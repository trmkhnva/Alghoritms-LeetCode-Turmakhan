class MinStack:

    def __init__(self):
        # основной стек
        self.stack = []
        # стек для хранения минимумов
        self.min_stack = []

    def push(self, val: int) -> None:
        # добавляем элемент в основной стек
        self.stack.append(val)

        # если стек минимумов пустой или новый элемент меньше
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # если удаляемый элемент равен минимуму
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        # удаляем из основного стека
        self.stack.pop()

    def top(self) -> int:
        # возвращает верхний элемент
        return self.stack[-1]

    def getMin(self) -> int:
        # минимальный элемент хранится во втором стеке
        return self.min_stack[-1]