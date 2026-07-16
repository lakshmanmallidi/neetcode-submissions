from collections import deque
class Solution:
    @staticmethod
    def printQueue(que, nums):
        print([nums[i] for i in list(que)[:10]])
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        lim = 0
        i=0
        while i<k:
            if(len(q)>0):
                while len(q)>0 and nums[q[-1]]<nums[i]:
                    q.pop()
                q.append(i)
            else:
                q.append(i)
            i=i+1
            #Solution.printQueue(q, nums)
        out = [nums[q[0]]]
        #Solution.printQueue(q, nums)
        while i<len(nums):
            if q[0]<i-k+1:
                q.popleft()
            print(nums[i])
            while len(q)>0 and nums[i]>nums[q[-1]]:
                q.pop()
            q.append(i)
            out.append(nums[q[0]])
            i=i+1
            #Solution.printQueue(q, nums)
            lim = lim+1
            #if(lim>100):
            #    break
        return out
        