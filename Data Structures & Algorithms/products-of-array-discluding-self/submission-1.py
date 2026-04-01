class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        dem, tich =  0, 1

        for i in range(len(nums)):
            if nums[i] == 0:
                dem += 1
            else: tich *= nums[i]

        res = []

        if dem == 0:
            for i in range(len(nums)):
                res.append(tich // nums[i])
            return res
                
        elif dem == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    res.append(tich)
                else: res.append(0)
            return res
        
        else: 
            return [0] * len(nums)
