class MinStack:

    def __init__(self):
        self.arr = []
        self.min_arr = []
        self.curr_min = 2**31 - 1
    
    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.curr_min > val:
            self.curr_min = val
        self.min_arr.append(self.curr_min)
        #print(self.arr, self.min_arr)

    def pop(self) -> None:
        self.arr.pop()
        self.min_arr.pop()
        if len(self.min_arr) > 0:
            self.curr_min = self.min_arr[-1]
        else:
            self.curr_min = 2**31 - 1
        #print("pop", self.arr, self.min_arr)

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.curr_min
