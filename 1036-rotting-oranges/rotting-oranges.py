from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # Очередь, куда будем складывать гнилые апельсины
        queue = deque()
        fresh = 0
        
        # Считаем свежие и запоминаем, где уже лежат гнилые
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        # Если свежих нет, то и ждать не надо
        if fresh == 0:
            return 0
            
        minutes = 0
        # Пока в очереди есть гнилые апельсины и есть кого заражать
        while queue and fresh > 0:
            minutes += 1
            # Проходим по всем апельсинам, которые гниют прямо сейчас
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                # Проверяем соседей (вверх, вниз, влево, вправо)
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    # Если нашли свежий апельсин — заражаем его
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
        
        # Если свежие остались — значит, до них не дотянулись
        return minutes if fresh == 0 else -1