class Solution:    
    def twoSum(self,nums,target):
        length=len(nums)
        for x in range(length-1):
            for y in range(x+1,length):
                if target==(nums[x]+nums[y]):
                    return x,y
        return "error"
