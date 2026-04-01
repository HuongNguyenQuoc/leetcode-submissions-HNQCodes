class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Method 1: Stack (LIFO)
        stack = [] #pair (temperatures, index)
        answer = [0] * len(temperatures)
        for i, t in enumerate(temperatures): #O(n)
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() #O(1)
                answer[stackInd] = i - stackInd
            stack.append((t, i)) #O(1)
        return answer
        '''
    #Time Complexity: O(n)
    #Space Complexity: O(n)
        
        #Method 2: DP
        n = len(temperatures)
        res = [0] * n #Space: O(n)
        for i in range(n - 2, -1, -1): #Time: O(n)
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    j = n
                    break
                j += res[j]
            if j < n:
                res[i] = j - i
        return res