class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        hash_map = {}
        max_len = 0
        ss = ""
        idx=0
        for i in range(0, len(s)):
            if s[i] not in hash_map:
                ss=ss+s[i]
            else:
                if(hash_map[s[i]]>=idx):
                    max_len = max(max_len, len(ss))
                    idx = hash_map.pop(s[i])
                    ss=s[idx+1:i+1]
                else:
                    ss=ss+s[i]
            hash_map[s[i]]=i
            print(ss)
        max_len = max(max_len, len(ss))
        return max_len
