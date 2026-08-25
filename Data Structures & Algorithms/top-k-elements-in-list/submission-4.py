import heapq
from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums))]
        for key, value in Counter(nums).items():
            buckets[value-1].append(key)
        #print(buckets)
        result = []
        j=0
        for i in range(len(nums)-1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                j = j+1
                if j==k:
                    return result
            #print(result,j,k)
