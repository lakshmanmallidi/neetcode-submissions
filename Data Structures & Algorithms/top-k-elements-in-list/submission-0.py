class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]=freq[nums[i]]+1
            else:
                freq[nums[i]]=1
        freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
        out = []
        i=0
        while i < k and i < len(freq):
            out.append(freq[i][0])
            i=i+1
        return out