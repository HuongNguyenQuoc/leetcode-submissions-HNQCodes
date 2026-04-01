import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        maxFreq = max(freq)
        maxCount = 0
        for x in freq:
            if x == maxFreq:
                maxCount += 1
        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)
        '''
        if n == 0:
            return len(tasks)

        count = Counter(tasks)#O(m) m: là chiều dài của tasks
        maxHeap = [-val for val in count.values()] #O(k)
        heapq.heapify(maxHeap)#O(k)
        time = 0
        cooldown = deque()

        while maxHeap or cooldown: #O(L): L là số lần vòng lặp chạy time lần
            time += 1

            if maxHeap:
                a = heapq.heappop(maxHeap) #O(log(k))
                a += 1
                if a != 0:
                    cooldown.append((time + n + 1, a))
            
            if cooldown and cooldown[0][0] == time + 1:
                _, remain = cooldown.popleft()
                heapq.heappush(maxHeap, remain)#O(log(k))
        
        return time



