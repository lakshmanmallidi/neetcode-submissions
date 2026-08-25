import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_cnt = [(-value,key) for key, value in Counter(nums).items()]
        heapq.heapify(freq_cnt)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(freq_cnt)[1])
        return result