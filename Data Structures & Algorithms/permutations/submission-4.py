class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        used = [False] * len(nums)
        res, path = [], []

        def backtrack():
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                #Allow append into path
                    path.append(nums[i])
                    used[i] = True
                    backtrack()
                    path.pop()
                    used[i] = False
        backtrack()
        return res

#TimeCP: O(n*n!)
#SpaceCP: O(n*n!) include list ouput.
'''
        if len(nums) == 0:
            return [[]]
        
        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1): #vị trí cần chèn
                tmp = p.copy()
                tmp.insert(i, nums[0])
                res.append(tmp)
        return res 