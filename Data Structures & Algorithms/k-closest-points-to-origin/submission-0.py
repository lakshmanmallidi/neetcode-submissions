class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for x, y in points:
            # 1. Calculate squared distance (negated for Max-Heap behavior)
            dist = -(x**2 + y**2)
            
            # 2. Push onto our heap
            heapq.heappush(max_heap, (dist, [x, y]))
            
            # 3. If we have more than k elements, discard the farthest one
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # 4. Extract the points out of our (distance, point) tuples
        return [point for dist, point in max_heap]
        