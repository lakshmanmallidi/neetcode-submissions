import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        inverted_stones = [stone * -1 for stone in stones]
        heapq.heapify(inverted_stones)
        while len(inverted_stones)>1:
            print("before smash",inverted_stones)
            y = heapq.heappop(inverted_stones)*-1
            x = heapq.heappop(inverted_stones)*-1
            if y-x > 0:
                heapq.heappush(inverted_stones,(y-x)*-1)
        if len(inverted_stones)>0:
            return heapq.heappop(inverted_stones) * -1
        else:
            return 0