import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        count = len(points)
        #очередь с приоритетом
        edges = [(0, 0)] 
        connected = set()
        total_cost = 0
        
        while len(connected) < count:
            cost, u = heapq.heappop(edges)
            
            # Если точку уже соединили, пропускаем
            if u in connected:
                continue
            
            # Добавляем стоимость и помечаем точку
            total_cost += cost
            connected.add(u)
            
            # Проверяем все остальные точки, чтобы найти ближайшую
            for v in range(count):
                if v not in connected:
                    #Считаем расстояние
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(edges, (dist, v))
                    
        return total_cost