class Solution:
    def rob(self, nums: List[int]) -> int:
        # Если домов нет, уносим ноль
        if not nums:
            return 0
        
        den1 = 0 # Максимум через один дом назад
        den2 = 0 # Максимум в предыдущем доме
        
        for dengi in nums:
            seychas = max(den2 + dengi, den1)
            
            # Сдвигаем значения
            den2 = den1
            den1 = seychas
            
        return den1