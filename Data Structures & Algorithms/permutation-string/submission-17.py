class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_encoding = [0] * 26
        for s in s1:
            target_encoding[ord(s) - ord('a')] += 1
        
        k = len(s1)

        encoding = [0] * 26
        for s in s2[:k]:
            encoding[ord(s) - ord('a')] += 1

        print(f"target_encoding: {s1}: {target_encoding}")
        print(f"initial encoding: {s2[:k]}: {encoding}")
        l, r = 0, k - 1
        while l < len(s2) - k + 1 and r < len(s2):
            if target_encoding == encoding: return True
            encoding[ord(s2[l]) - ord('a')] -= 1
            l+=1
            r+=1
            if r < len(s2): encoding[ord(s2[r]) - ord('a')] += 1
            print(f"curr encoding: {s2[l:r+1]}: {encoding}")
        
        return False



