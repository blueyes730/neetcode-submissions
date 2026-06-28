class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None: return True
        if len(s) == 1: return True
        pal = "".join(c.lower() for c in s if c.isalnum())
        l,r = 0, len(pal) - 1

        while l < r:
            if pal[l] != pal[r]: return False
            l += 1
            r -= 1
        return True
        