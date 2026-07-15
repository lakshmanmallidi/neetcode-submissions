class Solution:
    @staticmethod
    def getMaxEleFreq(counter):
        if len(counter) > 0:
            return sorted(counter.items(), key=lambda x:x[1], reverse=True)[0][1]
        else:
            return 0
    
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        j=0
        counter = {}
        max_window = 1
        while i < len(s) and j < len(s):
            if s[j] in counter:
                counter[s[j]] = counter[s[j]]+1
            else:
                counter[s[j]] = 1
            ws = j-i+1
            maxEleFreq = Solution.getMaxEleFreq(counter)
            print(counter, "window_size=",ws,"maxEleFreq=",maxEleFreq,"max_window=",max_window)
            print("*******************************")
            if (ws-maxEleFreq)<=k:
                max_window = max(max_window, ws)
                j=j+1
            else:
                counter[s[i]] = counter[s[i]] - 1
                i = i+1
                j = j+1
        return max_window
        