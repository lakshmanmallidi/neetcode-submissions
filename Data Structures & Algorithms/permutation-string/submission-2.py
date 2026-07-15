class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ws = len(s1)
        s1_sorted = sorted(s1)
        i=0
        j=ws
        while j <= len(s2):
            ss = s2[i:j]
            print(ss)
            if(sorted(ss)==s1_sorted):
                return True
            else:
                i=i+1
                j=j+1
        return False