class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        min_ele = 1000
        min_idx = 0
        while i<=j:
            m = (i+j)//2
            if nums[m]<=nums[-1]:
                j = m-1
            else:
                i = m+1
            if nums[m]<min_ele:
                min_ele = nums[m]
                min_idx = m
        if target == nums[0]:
            return 0
        if target >= nums[0] and target <= nums[min_idx-1] and min_idx>0:
            i = 0
            j = min_idx-1
        else:
            i = min_idx
            j = len(nums)-1
        print(i,j)
        while i<=j:
            m = (i+j)//2
            if nums[m]==target:
                return m
            elif target>nums[m]:
                i = m+1
            else:
                j=m-1
        return -1
