class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last, res = {}, []
        end, cnt = -1, 0
        
        # Build hashMap for each letter we need find the last index it's show up in original string
        for i, ch in enumerate(s):
            last[ch] = i
        
        # We need check where the portition match index so we add them into res
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            cnt += 1
            if i == end:
                res.append(cnt)
                end, cnt = -1, 0
        
        return res