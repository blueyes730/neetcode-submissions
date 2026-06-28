class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []

        def recursive(opened, closed):
            if opened == closed == n:
                ret.append("".join(stack))
            if opened < n:
                stack.append("(")
                recursive(opened + 1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                recursive(opened, closed + 1)
                stack.pop()
        recursive(0,0)
        return ret