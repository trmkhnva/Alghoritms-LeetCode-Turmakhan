class Solution:
    def climbStairs(self, n: int) -> int:
        # Если ступенек меньше или равно 2, то количество способов равно количеству ступенек
        if n <= 2:
            return n
        
        v1 = 1
        v2 = 2
        
        # Идем от 3-й ступеньки до n
        for i in range(3, n + 1):
            # Считаем текущее количество способов
            tekushiy = v1 + v2
            # Сдвигаем значения для следующего шага
            v1 = v2
            v2 = tekushiy
            
        return v2