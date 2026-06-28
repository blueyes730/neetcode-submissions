class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ret = []

        def recurse(numOpen, numClose):
            # three cases: 
            # 1) open == close == n, append to ret
            if numOpen == numClose == n:
                ret.append("".join(stack))
                return
            # 2) open < n, append an open parenthesis
            if numOpen < n:
                stack.append("(")
                recurse(numOpen + 1, numClose)
                stack.pop() # reset when done
            # 3) close < open, append a close parenthesis
            if numClose < numOpen:
                stack.append(")")
                recurse(numOpen, numClose + 1)
                stack.pop() # reset when done
        recurse(0,0)
        return ret