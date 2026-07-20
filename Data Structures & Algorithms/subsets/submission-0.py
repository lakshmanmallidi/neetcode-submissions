class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtracking(i, sub_arr):
            if i >= len(nums):
                result.append(sub_arr.copy())
                return
            sub_arr.append(nums[i])
            backtracking(i+1, sub_arr)
            sub_arr.pop()
            backtracking(i+1, sub_arr)
        backtracking(0, [])
        return result