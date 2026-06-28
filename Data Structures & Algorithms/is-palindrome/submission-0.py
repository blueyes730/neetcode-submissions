class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = s.replace(' ', '').lower()
        newstr = ''.join(c for c in newstr if c.isalnum())
        
        i = 0
        j = len(newstr)-1
        
        while (i<=j):
            if newstr[i]!= newstr[j]:
                return False
            i+=1
            j-=1
        return True

