class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        valid={
            '[':']',
            '(':')',
            '{':'}'
        }
        for ch in s:
            if ch in valid:
                stack.append(ch)
            else:
                if not stack:
                    return False
                popped=stack.pop()
                if ch!=valid[popped]:
                    return False
        return not stack