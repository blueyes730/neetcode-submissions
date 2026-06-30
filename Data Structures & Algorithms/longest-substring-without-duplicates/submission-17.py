class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        idx_lookup = {}
        max_len = 0

        for r in range(len(s)):
            if s[r] in idx_lookup:
                # move l to in front of that last occurence of s[r]
                # s[r] canbe inside window, so l moves forward,
                # s[r] can also be outside window, where l would move backwards <- bad
                l = max(l, idx_lookup[s[r]] + 1)
            
            idx_lookup[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len
