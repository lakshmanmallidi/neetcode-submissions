class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix) - 1
        m = -1
        while i<=j:
            mid = (j+i)//2
            if target >= matrix[mid][0] and target<=matrix[mid][-1]:
                m = mid
                break
            elif target > matrix[mid][-1]:
                i = mid + 1
            else:
                j = mid - 1
        if m == -1:
            return False
        arr = matrix[m]
        i=0
        j = len(arr)-1
        n = -1
        while i<=j:
            mid = (j+i)//2
            if target == arr[mid]:
                n = mid
                break
            elif target > arr[mid]:
                i = mid + 1
            else:
                j = mid - 1
        if n==-1:
            return False
        return True