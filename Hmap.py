class Solution(object):
    def twoSum(self, nums, target):
        hmap=dict()
        n=len(nums)
        current_id=0

        for i in range(n):
            CurNum=nums[i]
            diff=target-CurNum
            if CurNum in hmap:
                return [hmap[CurNum],i]
            else:
                hmap[diff]=i
