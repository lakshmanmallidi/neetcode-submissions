class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        out = []
        while i <= len(nums)-k:
            out.append(max(nums[i:i+k]))
            i=i+1
        return out