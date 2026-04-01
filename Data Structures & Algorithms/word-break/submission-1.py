class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordSet = set(wordDict)
        n = len(s)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == n:
                return True
            res = ""
            for j in range(i, n):
                res += s[j]
                if res in wordSet and dfs(j + 1):
                    cache[i] = True
                    return True
            cache[i] = False
            return False
        
        return dfs(0)