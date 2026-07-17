class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        min_ele = 1000
        while i<=j:
            m = (i+j)//2
            if nums[m]<=nums[-1]:
                j = m-1
            else:
                i = m+1
            if nums[m]<min_ele:
                min_ele = nums[m]
        return min_ele