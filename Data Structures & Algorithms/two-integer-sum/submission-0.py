class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals={}
        for x,y in enumerate(nums):
            need=target-y
            if need in vals:
                return [vals[need],x]
            else:
                vals[y]=x

        