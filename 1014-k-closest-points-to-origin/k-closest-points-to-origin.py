import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            dist = -(x**2 + y**2)   # отрицательное расстояние для max-heap
            heapq.heappush(heap, (dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        return [point for dist, point in heap]