# https://leetcode.com/problems/time-based-key-value-store/

class TimeMap1: # T: 25.60% M: 60.43%

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp,value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""
        res = -1
        left, right = 0, len(self.store[key]) - 1
        while left <= right:
            mid = (right + left) // 2
            if self.store[key][mid][0] == timestamp:
                return self.store[key][mid][1]
            elif self.store[key][mid][0] < timestamp:
                if self.store[key][mid][0] > res:
                    res = mid
                left = mid + 1
            else:
                right = mid - 1
        if res == -1:
            return "" 
        else:
            return self.store[key][res][1]

class TimeMap2: # T: 57.86% M: 85.06%

    def __init__(self):
        self.store = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp,value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.store:
            return ""
        arr = self.store[key]
        res = -1
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (right + left) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                if arr[mid][0] > res:
                    res = mid
                left = mid + 1
            else:
                right = mid - 1
        if res == -1:
            return "" 
        else:
            return arr[res][1]