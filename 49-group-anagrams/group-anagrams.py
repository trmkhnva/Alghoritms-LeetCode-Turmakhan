class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        d = {}  # словарь
        
        for word in strs:
            key = ''.join(sorted(word))  # сортируем буквы
            
            if key not in d:
                d[key] = []
            
            d[key].append(word)
        
        return list(d.values())