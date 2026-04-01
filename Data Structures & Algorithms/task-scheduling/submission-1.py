class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        store = [0] * 26
        for task in tasks:
            store[ord(task) - ord('A')] += 1
        maxCount = max(store)
        maxFreq = 0
        for val in store:
            if val == maxCount:
                maxFreq += 1
        return max(len(tasks), (maxCount - 1) * (n + 1) + maxFreq)
        