class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def recursion(nums):
            print(nums)
            if len(nums)==1:
                if nums[0][1] == target:
                    return nums[0][0]
                else:
                    return -1
            mid = len(nums)//2
            print(mid)
            if target >= nums[mid][1]:
                return recursion(nums[mid:])
            else:
                return recursion(nums[:mid])
        return recursion(list(enumerate(nums)))