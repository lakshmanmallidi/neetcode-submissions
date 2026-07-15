class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        hash_map = {}
        max_len = 1
        ss = 0
        idx=0
        for i in range(0, len(s)):
            if s[i] not in hash_map:
                max_len = max(max_len, i+1-idx)
            else:
                if(hash_map[s[i]]>=idx):
                    max_len = max(max_len, i-idx) 
                    idx = hash_map.pop(s[i])+1
            hash_map[s[i]]=i
            print(hash_map," i=",i, "idx=",idx, "max_len=",max_len)
        max_len = max(max_len,ss)
        return max_len
