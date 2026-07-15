class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        current = {}
        for char in t:
            if char in target:
                target[char]=target[char]+1
            else:
                target[char]=1
                current[char]=0
        target_cnt = len(target)
        current_cnt = 0
        i=0
        j=0
        min_ss=1000
        min_i = 0
        min_j = 0
        while i<len(s) and j<len(s):
            if target_cnt != current_cnt:
                if s[j] in current:
                    current[s[j]]=current[s[j]]+1
                    if(current[s[j]]==target[s[j]]):
                        current_cnt = current_cnt+1
                j = j+1
            else:
                if j-i < min_ss:
                    min_i = i
                    min_j = j
                    min_ss = j-i
                if s[i] in current:
                    current[s[i]]=current[s[i]]-1
                    if(current[s[i]]<target[s[i]]):
                        current_cnt = current_cnt-1
                i = i+1
            #print("current=", current," current_cnt=",current_cnt, " j=",j, " i=",i, " min_ss=",min_ss, " ss=", s[min_i:min_j])
            #print("******************************************")
        while i<len(s) and target_cnt==current_cnt:
            if j-i < min_ss:
                min_i = i
                min_j = j
                min_ss = j-i
            if s[i] in current:
                current[s[i]]=current[s[i]]-1
                if(current[s[i]]<target[s[i]]):
                    current_cnt = current_cnt-1
            i = i+1

        return s[min_i:min_j]
        