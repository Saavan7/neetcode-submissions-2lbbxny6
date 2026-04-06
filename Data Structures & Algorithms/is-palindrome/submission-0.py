class Solution:
    def isPalindrome(self, s: str) -> bool:
        b=''.join(i.lower() for i in s if i.isalnum())
        return b==b[::-1]
            
        