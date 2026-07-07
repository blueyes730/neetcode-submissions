class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m.setdefault(key, []).append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.m.get(key, [])
        l, r = 0, len(vals) - 1
        ret = ""

        while l <= r:
            mid = l + ((r-l)//2)
            midval, midtime = vals[mid]
            if midtime > timestamp:
                r = mid - 1
            else:
                ret = midval
                l = mid + 1
    
        return ret

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)