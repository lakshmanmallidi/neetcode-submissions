class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==1 and strs[0]=="":
            return "3$nan"
        return "3$".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        elif s == "3$nan":
            return [""]
        return s.split("3$")