class Solution:
    def isPalindrome(self, s: str) -> bool:
        strg = ""
        strg_rev = ""
        l = len(s)
        for i in range(l):
            v1 = ord(s[i].lower())
            if ((v1>=97 and v1<=122) or (v1>=48 and v1<=57)):
                strg = strg+s[i].lower()
            v2 = ord(s[l-i-1].lower())
            if ((v2>=97 and v2<=122) or (v2>=48 and v2<=57)):
                strg_rev = strg_rev+s[l-i-1].lower()
        return strg==strg_rev