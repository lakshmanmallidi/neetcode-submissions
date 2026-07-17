class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merged = []
        while i<len(nums1) and j<len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i=i+1
            else:
                merged.append(nums2[j])
                j=j+1
        while i < len(nums1):
            merged.append(nums1[i])
            i=i+1
        while j < len(nums2):
            merged.append(nums2[j])
            j=j+1
        l = len(nums1)+len(nums2)
        print(merged)
        if l%2 ==0:
            a = merged[(l//2)]
            b = merged[(l//2)-1]
            return (a+b)/2
        else:
            return merged[l//2]
        return 0

        