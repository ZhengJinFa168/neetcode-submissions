class TimeMap:

    def __init__(self):
        self.dict_val = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dict_val:
            self.dict_val[key] = [[],[]]
        self.dict_val[key][0].append(value)
        self.dict_val[key][1].append(timestamp)
        return

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_val:
            return ""
        res = ""
        l,r = 0,len(self.dict_val[key][0]) - 1
        while l <= r:
            mid = (r + l) // 2
            if self.dict_val[key][1][mid] <= timestamp:
                res = self.dict_val[key][0][mid]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
