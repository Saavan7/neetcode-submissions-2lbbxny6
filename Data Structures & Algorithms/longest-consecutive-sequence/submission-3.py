class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for i in nums:
            if i-1 not in nums:
                current=1
                while i+1 in nums:
                    current+=1
                    i+=1
                longest=max(longest,current)
        return longest