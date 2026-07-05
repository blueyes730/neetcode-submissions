class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for c in s:
            # first check if you have opening brace
            if c in mapping: stack.append(c)
            else:
                # closing brace behavior
                # if stack is empty at anytime, then there is no opening brace to counteract the closing brace so return false early
                if not stack: return False
                # if you have a closing brace and the top of the stack is not the matching opening brace, this is an invalid string
                if mapping[stack.pop()] != c: return False
        return not stack