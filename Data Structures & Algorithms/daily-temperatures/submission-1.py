class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0]*len(temperatures)
        stack = [0]
        i=1
        while i < len(temperatures):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last_i = stack.pop()
                out[last_i]=i-last_i
            stack.append(i)
            #print(stack)
            i=i+1
        return out