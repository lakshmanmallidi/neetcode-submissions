from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        que.append(nums[0])
        i = 0
        j = 1
        result = []
        while j < k:
            while len(que)>0 and que[-1] < nums[j]:
                que.pop()
            que.append(nums[j])
            j = j+1
        result.append(que[0])
        while j < len(nums):
            if que[0] == nums[i]:
                que.popleft()
            i = i+1
            while len(que)>0 and que[-1] < nums[j]:
                que.pop()
            que.append(nums[j])
            j = j+1
            result.append(que[0])
        return result
