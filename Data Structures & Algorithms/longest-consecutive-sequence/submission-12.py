class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums_p = set(nums)
        max_l = 1
        prev_max_start = prev_max_end = -10**9
        for num in nums:
            if (num-1) in nums_p and not (num >=prev_max_start and num<=prev_max_end):
                print(num)
                start = num
                max_curr = 1
                while num in nums_p:
                    if num+1>=prev_max_start and num+1<=prev_max_end:
                        max_curr = max_curr+max_l
                        break
                    max_curr = max_curr+1
                    num = num+1
                end = num-1
                if(max_l<max_curr):
                    prev_max_start = start
                    prev_max_end = end
                    print(prev_max_start, prev_max_end)
                    max_l = max_curr
        return max_l
