class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ws = len(s1)
        s1_sorted = sorted(s1)
        j=ws
        ss=s2[0:j]
        while j < len(s2):
            if(sorted(ss)==s1_sorted):
                return True
            else:
                ss = ss[1:]+s2[j]
                j=j+1
        if(sorted(ss)==s1_sorted):
            return True
        return False