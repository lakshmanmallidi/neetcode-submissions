class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for i in range(len(tokens)):
            if tokens[i] not in ('+','*','-','/'):
                arr.append(int(tokens[i]))
            else:
                if tokens[i] == "+":
                    a = arr.pop()
                    b = arr.pop()
                    arr.append(b+a)
                elif tokens[i] == "-":
                    a = arr.pop()
                    b = arr.pop()
                    arr.append(b-a)
                elif tokens[i] == "*":
                    a = arr.pop()
                    b = arr.pop()
                    arr.append(a*b)
                else:
                    a = arr.pop()
                    b = arr.pop()
                    arr.append(int(b/a))
            print(arr)
        return arr[-1]