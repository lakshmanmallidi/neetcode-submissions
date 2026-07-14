class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}
        i=j=0
        print(len(s))
        print(len(t))
        while i < len(s) and j < len(t):
            if s[i]==t[j]:
                i = i+1
                j = j+1
            else:
                if t[j] in hash_map:
                    if(hash_map[t[j]]>1):
                        hash_map[t[j]] = hash_map[t[j]] - 1
                    else:
                        hash_map.pop(t[j])
                    j=j+1
                if s[i] in hash_map:
                    hash_map[s[i]]=hash_map[s[i]] + 1
                else:
                    hash_map[s[i]] = 1
                i=i+1
        #print(i, j, hash_map)
        while j < len(t):
            if t[j] in hash_map:
                if(hash_map[t[j]]>1):
                    hash_map[t[j]] = hash_map[t[j]] - 1
                else:
                    hash_map.pop(t[j])
            else:
                return False
            j=j+1
        #print(i, j, hash_map)
        if len(s)>i or len(hash_map)>0:
            return False
        else:
            return True