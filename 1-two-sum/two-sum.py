class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} 
        for i, num in enumerate(nums): # присваивает индексы числу
            coll = target - num # target - цель, num  - половина цели, coll - недостающее число
            if coll in num_map: # проверка
                return [num_map[coll], i]
            num_map[num] = i