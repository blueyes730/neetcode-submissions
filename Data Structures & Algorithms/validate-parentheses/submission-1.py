class Solution:
    def isValid(self, s: str) -> bool:
        punc = {')':'(', ']':'[', '}':'{'}
        st = []
        if len(s) % 2 != 0: return False

        for c in s:
            if c in punc:
                if st and st[-1] == punc[c]:
                    st.pop()
                else: return False
            else: 
                st.append(c)        
        return not st

