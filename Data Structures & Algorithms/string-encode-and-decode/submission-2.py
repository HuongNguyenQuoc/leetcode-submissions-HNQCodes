class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += len(s) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
