from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            anagram = [0] * 26
            for l in word:
                anagram[ord(l) - ord('a')] += 1

            anagrams[tuple(anagram)].append(word)
        
        return list(anagrams.values())
            

            


