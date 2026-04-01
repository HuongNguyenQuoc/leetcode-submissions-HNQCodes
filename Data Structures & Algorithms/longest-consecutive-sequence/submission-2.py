class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        dic = {}
        longest = 1
        for n in nums:
            if n not in dic:
                left = dic.get(n - 1, 0)
                right = dic.get(n + 1, 0)
                total = left + right + 1

                dic[n] = total
                dic[n - left] = total
                dic[n + right] = total
                longest = max(total, longest)
        return longest

                