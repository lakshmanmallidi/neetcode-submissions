class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "[empty]"
        encoded_strg = strs[0]
        for i in range(1, len(strs)):
            encoded_strg = encoded_strg+':;'+strs[i]
        return encoded_strg

    def decode(self, s: str) -> List[str]:
        if s=="[empty]":
            return []
        strgs = []
        strg=""
        i=0
        while i<len(s):
            if s[i]==":" and s[i+1]==";":
                print(strg)
                strgs.append(strg)
                i=i+2
                strg=""
            else:
                strg = strg+s[i] 
                i=i+1  
        strgs.append(strg)     
        return strgs