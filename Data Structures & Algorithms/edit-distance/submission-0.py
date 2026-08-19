class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
      m, n = len(word1), len(word2)

      # dp[i][j] = minimum operations to convert
      # word1[i:] into word2[j:]
      dp = [[0] * (n + 1) for _ in range(m + 1)]

      # word1 is empty
      # Need to insert the remaining characters of word2
      for j in range(n + 1):
        dp[m][j] = n - j

      # word2 is empty
      # Need to delete the remaining characters of word1
      for i in range(m + 1):
        dp[i][n] = m - i

      # Fill the table from bottom-right to top-left
      for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
          if word1[i] == word2[j]:
            dp[i][j] = dp[i + 1][j + 1]
          else:
            dp[i][j] = 1 + min(
              dp[i + 1][j],
              dp[i][j + 1],
              dp[i + 1][j + 1]
            )
      
      return dp[0][0]