from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Helper: compute total hours needed if speed = k
        def hours_needed(k: int) -> int:
            total = 0
            for p in piles:
                total += (p + k - 1) // k  # ceil(p / k)
            return total

        left, right = 1, max(piles)  # search k in [1..max(piles)]
        answer = right

        while left <= right:
            mid = (left + right) // 2
            if hours_needed(mid) <= h:
                answer = mid          # mid works, try smaller k
                right = mid - 1
            else:
                left = mid + 1        # mid too slow, need bigger k

        return answer
