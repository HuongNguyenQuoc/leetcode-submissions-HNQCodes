class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Resolve first row
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        # Resolve first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        
        # Resolve every single cell in grid and finally we return dp[m][n]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                take_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                take_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = take_s1 or take_s2
        
        return dp[m][n]
