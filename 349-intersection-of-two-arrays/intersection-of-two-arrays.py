class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        
        set1 = set(nums1)   # делаем множество из первого массива
        result = set()      # чтобы не было повторений
        
        # проходим по второму массиву
        for num in nums2:
            if num in set1:     # если есть в первом
                result.add(num) # добавляем в ответ
        
        return list(result)