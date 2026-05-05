class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l,longest=0,0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[i])
            longest=max(longest,i-l+1)
        return longest
            
        