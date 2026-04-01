class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, countT = {}, {}

        for x in t:
            countT[x] = countT.get(x, 0) + 1
        
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1, -1], 10**19

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l , r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != 10**19 else ""


