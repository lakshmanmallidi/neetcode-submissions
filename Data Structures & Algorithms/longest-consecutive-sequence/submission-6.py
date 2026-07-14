class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums_p = set(nums)
        max_l = 1
        for num in nums:
            if (num-1) in nums_p:
                max_curr = 1
                while num in nums_p:
                    max_curr = max_curr+1
                    num = num+1
                if(max_l<max_curr):
                    max_l = max_curr
        return max_l
