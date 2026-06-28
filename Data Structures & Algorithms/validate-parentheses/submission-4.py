class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {")":"(", "]": "[", "}":"{"}

        if len(s) % 2 != 0: return False

        for c in s:
            if c in m:
                if stack and m[c] == stack[-1]: stack.pop()
                else: return False
            
            else: stack.append(c)
        return not stack