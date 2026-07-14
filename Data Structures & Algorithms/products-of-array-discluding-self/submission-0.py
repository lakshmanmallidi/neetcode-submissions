class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        no_zeros = 0
        for num in nums:
            if num!=0:
                total = total * num
            else:
                no_zeros=no_zeros+1
        if no_zeros == 0:
            return [int(total/num) for num in nums if num!=0]
        elif no_zeros == 1:
            return [total if num==0 else 0 for num in nums] 
        else:
            return [0]*len(nums)