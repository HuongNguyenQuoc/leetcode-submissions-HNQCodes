class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashMap = {}
        count = 0
        for num in nums:
            count += hashMap.get(num, 0)
            hashMap[num] = hashMap.get(num, 0) + 1
        return count