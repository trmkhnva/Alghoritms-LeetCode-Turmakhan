import heapq

class Solution:
    def lastStoneWeight(self, stones):
        heap = [-s for s in stones]  # max-heap через отрицания
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, -(first - second))

        return -heap[0] if heap else 0