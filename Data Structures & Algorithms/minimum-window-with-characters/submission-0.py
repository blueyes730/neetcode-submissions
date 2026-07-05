class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointer
        # let l be at 0 initially
        # iterate r till you have all necessary letters of t
        # when window has all letters, iterate l till window 
        #   no longer has all letters of t
        # Use maps to store t char and window char
        #   since string can have both upper and lower case so 
        #   we cannot use binary char list

        if (
            (len(t) > len(s))
            or (t is None) 
            or (s is None) 
            or (len(t) == 0) 
            or (len(s) == 0)
        ): 
            return ""
            
        window, char_t = {}, {}

        for c in t:
            char_t[c] = char_t.get(c, 0) + 1

        l, minlen = 0, len(s) + 1 
        bounds = [-1, -1]
        have, need = 0, len(char_t)

        for r in range(len(s)):
            curr_char = s[r]
            window[curr_char] = window.get(curr_char, 0) + 1
            if curr_char in char_t and char_t[curr_char] == window[curr_char]:
                have += 1
            
            while have == need:
                if r - l + 1 < minlen:
                    bounds = [l, r]
                    minlen = r - l + 1 
                
                removed_char = s[l]
                window[removed_char] -= 1
                if removed_char in char_t and char_t[removed_char] > window[removed_char]:
                    have -= 1

                l += 1
            
        l, r = bounds
        return s[l: r+1]
        

        



