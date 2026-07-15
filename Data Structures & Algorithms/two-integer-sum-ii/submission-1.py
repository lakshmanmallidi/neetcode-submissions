class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        boundary = len(numbers)-1
        i=0
        while i<boundary:
            if numbers[i]+numbers[boundary]==target:
                return [i+1, boundary+1]
            elif numbers[i]+numbers[boundary]>target:
                boundary=boundary-1
            else:
                i=i+1
        