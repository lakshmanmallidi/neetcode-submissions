class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        out = [1]*len(nums)
        for i in range(1, len(nums)):
            pre = pre*nums[i-1]
            out[i-1]=pre
        post = 1
        for i in range(len(nums)-1,0,-1):
            out[i]=post*out[i-1]
            post = post*nums[i]
        out[0]=post
        return out