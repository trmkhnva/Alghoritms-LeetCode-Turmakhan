class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        obshaya_summa = sum(nums)
        
        # Если сумма нечетная, пополам не поделить
        if obshaya_summa % 2 != 0:
            return False
        
        target = obshaya_summa // 2
        vozmozhnye_summy = {0}
        
        for chislo in nums:
            novye_summy = set()
            for s in vozmozhnye_summy:
                # Если мы добавим текущее число к уже известной сумме
                novaya_s = s + chislo
                if novaya_s == target:
                    return True
                if novaya_s < target:
                    novye_summy.add(novaya_s)
            
            # Объединяем старые суммы с новыми
            vozmozhnye_summy.update(novye_summy)
            
        return target in vozmozhnye_summy