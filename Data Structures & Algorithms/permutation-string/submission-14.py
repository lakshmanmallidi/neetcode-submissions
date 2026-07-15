class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_wc = [0] * 26
        s2_wc = [0] * 26
        ss = s2[:len(s1)]
        for e in s1:
            s1_wc[ord(e)-ord('a')] = s1_wc[ord(e)-ord('a')] +1
        for e in ss:
            s2_wc[ord(e)-ord('a')] = s2_wc[ord(e)-ord('a')] +1
        i=len(s1)
        while i < len(s2):
            if s1_wc == s2_wc:
                return True
            else:
                going = s2[i-len(s1)]
                coming = s2[i]
                s2_wc[ord(going)-ord('a')]=s2_wc[ord(going)-ord('a')]-1
                s2_wc[ord(coming)-ord('a')]=s2_wc[ord(coming)-ord('a')]+1
                i=i+1
        if s1_wc == s2_wc:
            return True
        return False