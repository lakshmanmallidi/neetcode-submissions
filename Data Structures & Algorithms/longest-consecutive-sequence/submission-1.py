class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        sorted_nums = sorted(nums)
        max_l = 0
        curr_max = 1
        for i in range(1,len(sorted_nums)):
            if(sorted_nums[i]==(sorted_nums[i-1]+1)):
                curr_max=curr_max+1
            elif(sorted_nums[i]==sorted_nums[i-1]):
                pass
            else:
                if curr_max > max_l:
                    max_l = curr_max
                curr_max = 1
        if curr_max > max_l:
            max_l = curr_max
        return max_l


        