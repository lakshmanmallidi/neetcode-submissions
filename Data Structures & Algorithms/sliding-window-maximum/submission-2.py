from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        i=0
        while i < k:
            q.append(nums[i])
            i=i+1
        out = [max(q)]
        while i < len(nums):
            q.popleft()
            q.append(nums[i])
            out.append(max(q))
            i=i+1
        return out