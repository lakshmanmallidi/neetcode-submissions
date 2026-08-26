class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while i<=j:
            ord_i = ord(s[i].lower())
            ord_j = ord(s[j].lower())
            print(s[i], s[j], ord_i, ord_j)
            if (ord_i >= 48 and ord_i <= 57) or (ord_i >= 97 and ord_i <= 122):
                if (ord_j >= 48 and ord_j <= 57) or (ord_j >= 97 and ord_j <= 122):
                    if s[i].lower()==s[j].lower():
                        i=i+1
                        j=j-1
                    else:
                        return False
                else:
                    j=j-1
            else:
                i=i+1
        return True