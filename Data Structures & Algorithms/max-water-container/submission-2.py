class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_v = 0
        i = 0
        j = len(heights)-1
        while i<j:
            if(heights[i]<=heights[j]):
                max_v = max(max_v, (j-i)*heights[i])
                i=i+1
            else:
                max_v = max(max_v, (j-i)*heights[j])
                j=j-1
        return max_v