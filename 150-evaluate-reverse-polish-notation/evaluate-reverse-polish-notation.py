class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []  # стек для хранения чисел

        for token in tokens:
            # если токен число, кладем в стек
            if token not in "+-*/":
                stack.append(int(token))
            else:
                # оператор: достаем два последних числа
                b = stack.pop()
                a = stack.pop()

                # выполняем операцию
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # деление округляется к нулю
                    stack.append(int(a / b))

        # результат в стеке
        return stack[0]

tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))