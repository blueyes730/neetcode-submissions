class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        ret = 0
        l = 0
        max_freq = 0
        for i in range(len(s)):
            freq[s[i]] =  1 + freq.get(s[i], 0)
            max_freq = max(max_freq, freq[s[i]])

            length = i-l+1

            if length - max_freq > k:
                freq[s[l]] -= 1
                l += 1
        
        return i-l+1 