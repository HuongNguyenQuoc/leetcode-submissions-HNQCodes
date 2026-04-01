from bisect import bisect_right

class TimeMap:
    def __init__(self):
        # key -> [(timestamp, value), ...]  (timestamps tăng dần)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        arr = self.store[key]  # list of (ts, val)
        # tìm vị trí phần tử cuối cùng có ts <= timestamp
        idx = bisect_right(arr, (timestamp, "\uffff")) - 1
        return arr[idx][1] if idx >= 0 else ""