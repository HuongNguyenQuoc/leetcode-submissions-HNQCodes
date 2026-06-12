class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        target = total // 2

        if target % 2:
            return False


        visited = set()
        visited.add(0)

        for num in nums:
            new_visited = visited.copy()

            for x in visited:
                new_visited.add(x + num)
            
            visited = new_visited

        return target in visited