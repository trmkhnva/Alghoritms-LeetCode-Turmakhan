class Solution:
    def isValid(self, s: str) -> bool:
        
        # стек для хранения открывающих скобок
        stack = []
        
        # соответствие закрывающих и открывающих скобок
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # проходим по строке
        for char in s:
            
            # если открывающая скобка — кладем в стек
            if char in "([{":
                stack.append(char)
            
            else:
                # если стек пуст — ошибка
                if not stack:
                    return False
                
                # берем последний элемент
                top = stack.pop()
                
                # проверяем соответствие
                if pairs[char] != top:
                    return False

        # если стек пуст — все скобки закрылись
        return len(stack) == 0