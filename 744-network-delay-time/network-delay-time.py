import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Строим карту 
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # Очередь с приоритетом 
        pq = [(0, k)]
        # Словарь для хранения самого быстрого времени до каждого узла
        visited = {}
        
        while pq:
            # Берем узел, до которого быстрее всего дошли
            time, node = heapq.heappop(pq)
            
            if node not in visited:
                visited[node] = time
                # Проверяем всех соседей этого узла
                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        # Считаем общее время до соседа
                        heapq.heappush(pq, (time + weight, neighbor))
                        
        # Если дошли до всех n узлов, берем самое долгое время
        if len(visited) == n:
            return max(visited.values())
        else:
            return -1