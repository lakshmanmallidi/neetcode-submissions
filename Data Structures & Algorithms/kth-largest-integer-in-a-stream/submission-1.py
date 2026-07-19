from collections import deque
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.buffer_length = k
        self.buffer = deque()
        for num in nums:
            self.stackInsert(num)

    def stackInsert(self, val):
        if len(self.buffer) == 0:
            self.buffer.append(val)
            return val
        temp_buffer = []
        while len(self.buffer)!=0 and val < self.buffer[-1]:
            temp_buffer.append(self.buffer.pop())
        self.buffer.append(val)
        while len(temp_buffer)!=0:
            self.buffer.append(temp_buffer.pop())
        if len(self.buffer)>self.buffer_length:
            self.buffer.popleft()
        return self.buffer[0]

    def add(self, val: int) -> int:
        out = self.stackInsert(val)
        print(self.buffer)
        return out