class Solution:
    def _isAlphaNumerical(self, char):
        char_ascii = ord(char.lower()) 
        if (char_ascii >= 48 and char_ascii <= 57) or \
            (char_ascii >= 97 and char_ascii <= 122):
            return True
        return False
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            while not self._isAlphaNumerical(s[l]) and l<r:
                l=l+1
            while not self._isAlphaNumerical(s[r]) and l<r:
                r=r-1
            if s[l].lower() != s[r].lower():
                return False
            l = l+1
            r = r-1
        return True