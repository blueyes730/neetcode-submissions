class Solution:
    def change(s1: str): 
        arr = [0] * 26
        for s in s1:
            arr[ord(s)-ord('a')] += 1
        return arr
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1) : return False
        arr = [0] * 26
        hashmap = {}

        arr = Solution.change(s1)
        for i in range(0, len(s2), 1):
            print(s2[i:(i+len(s1))])
            hashmap[s2[i:(i+len(s1))]] = Solution.change(s2[i:(i+len(s1))])
        
        print(hashmap)
        print(f"s1: {arr}")
        if arr in hashmap.values(): return True
        else: return False


                