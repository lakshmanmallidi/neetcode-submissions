class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                v = (j-i)*min(heights[i], heights[j])
                max_v = max(max_v,v)
        return max_v