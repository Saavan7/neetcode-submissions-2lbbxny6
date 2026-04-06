import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fin=[]
        prod=1
        for i in range(0,len(nums)):
            for j in range(0,i):
                prod*=nums[j]
            for k in range(i+1,len(nums)):
                prod*=nums[k]
            fin.append(prod)
            prod=1
        return fin


            

        
        