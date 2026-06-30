class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        freqMap = {}
        maxChar = 0

        l, r = 0, 0
        while r < len(s):
            freqMap[s[r]] = 1 + freqMap.get(s[r], 0)
            maxChar = max(maxChar, freqMap[s[r]])
            while (r - l + 1) - maxChar > k:
                freqMap[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        
        return max_len
