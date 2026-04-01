class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        longest = 1
        s = set(nums)
        for n in s:
            if n - 1 not in s:
                length = 1
                while n + length in s:
                    length += 1
                    longest = max(length, longest)
        return longest
                