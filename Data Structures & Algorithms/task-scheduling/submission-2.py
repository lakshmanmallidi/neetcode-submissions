from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnts = [-task_cnt for task_cnt in Counter(tasks).values()]
        heapq.heapify(task_cnts)
        t = 0
        wait = deque()
        while task_cnts or wait:
            t=t+1
            print(t, task_cnts, wait)
            if task_cnts:
                max_task = 1+heapq.heappop(task_cnts)
                if (max_task)*-1 > 0:
                    wait.append((max_task, t+n))
            if wait and wait[0][1]==t:
                heapq.heappush(task_cnts, wait.popleft()[0])
        return t