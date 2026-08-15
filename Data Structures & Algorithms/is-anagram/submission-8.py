class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        i = j = 0
        hash_set = {}
        while j < len(t) and i < len(s):
            #print(s[i], t[j], hash_set)
            if s[i]==t[j]:
                i=i+1
                j=j+1
            elif t[j] in hash_set:
                if hash_set[t[j]] > 1:
                    hash_set[t[j]]=hash_set[t[j]]-1
                else:
                    hash_set.pop(t[j])
                j=j+1
            elif s[i] in hash_set:
                hash_set[s[i]]=hash_set[s[i]]+1
                i=i+1
            else:
                hash_set[s[i]]=1
                i=i+1
        while j < len(t):
            if t[j] in hash_set:
                if hash_set[t[j]] > 1:
                    hash_set[t[j]]=hash_set[t[j]]-1
                else:
                    hash_set.pop(t[j])
            j = j+1
        if len(hash_set)>0:
            return False
        else:
            return True