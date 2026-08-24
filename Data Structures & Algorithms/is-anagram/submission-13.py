class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        miss_matches = {}
        i = j = 0
        while i<len(s) and j < len(t):
            if s[i]==t[j]: 
                j += 1
            else:
                if s[i] in miss_matches:
                    miss_matches[s[i]] += 1
                else:
                     miss_matches[s[i]] = 1
                if t[j] in miss_matches:
                    if miss_matches[t[j]] > 1:
                        miss_matches[t[j]] -= 1
                    else:
                        miss_matches.pop(t[j])
                    j += 1
            i += 1
            #print(miss_matches, i, j)
        while j < len(t):
            if t[j] in miss_matches:
                if miss_matches[t[j]] > 1:
                    miss_matches[t[j]] -= 1
                else:
                    miss_matches.pop(t[j])
            else:
                break
            j += 1
        #print(miss_matches, i, j)
        if len(miss_matches) > 0:
            return False
        else:
            return True


            