class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target):
            if len(nums)==1:
                if nums[0][1]==target:
                    return nums[0][0]
                else:
                    return -1

            mid = len(nums)//2
            
            idx = binary_search(nums[:mid], target)
            if idx != -1:
                return idx
            idx = binary_search(nums[mid:], target)
            if idx != -1:
                return idx
            
            return -1
    
        return binary_search(list(enumerate(nums)), target)
        
