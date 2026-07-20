class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, subarr, total):
            if total == target:
                result.append(subarr.copy())
                return

            if i>=len(nums) or total > target:
                return

            subarr.append(nums[i])
            dfs(i, subarr, nums[i]+total)
            subarr.pop()
            dfs(i+1, subarr, total)
        
        dfs(0, [], 0)
        return result