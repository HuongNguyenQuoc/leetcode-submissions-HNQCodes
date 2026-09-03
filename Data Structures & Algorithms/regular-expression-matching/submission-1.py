class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {} # cache: key = (i, j), value = True/False

        def dfs(i: int, j: int) -> bool:
            # if we already solved this (i, j) before, just return it
            if (i, j) in memo:
                return memo[(i, j)]

            # base case: pattern is empty
            if j == len(p):
                result = i == len(s)

            else:
                # check if s[i] matches p[j] (or p[j] is '.')
                first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

                # check if next char in pattern is '*'
                if j+1 < len(p) and p[j+1] == "*":
                    # two choices:
                        # 1. skip "x*" completely (use 0 times)
                        # 2. use current char (if first_match) and stay on same p[j] (use 1+ times)
                    result = dfs(i, j+2) or (first_match and dfs(i+1, j))
                else:
                    # normal case, move both pointers forward
                    result = first_match and dfs(i+1, j+1)

            memo[(i, j)] = result # save answer before returning
            return result

        return dfs(0, 0)