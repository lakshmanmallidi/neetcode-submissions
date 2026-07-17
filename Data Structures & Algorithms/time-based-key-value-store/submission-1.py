class TimeMap:

    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key]=[(value, timestamp)]
        else:
            self.hash_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hash_map:
            values = self.hash_map[key]
        else:
            return ""
        i=0
        j=len(values)-1
        while i<=j:
            m = (i+j)//2
            if values[m][1]==timestamp:
                return values[m][0]
            elif timestamp < values[m][1]:
                j = m - 1
            else:
                i = i + 1
        if j == -1:
            return ""
        return values[j][0]

