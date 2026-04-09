class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        
        def explore(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
                return
            
            #отмечаем что тут уже прошлись
            grid[r][c] = '0'
            
            # Проверяем всех соседей по кругу
            explore(r + 1, c) # низ
            explore(r - 1, c) # верх
            explore(r, c + 1) # право
            explore(r, c - 1) # лево
            
        # Проходимся по каждой клетке
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    count += 1
                    explore(r, c)
                    
        return count