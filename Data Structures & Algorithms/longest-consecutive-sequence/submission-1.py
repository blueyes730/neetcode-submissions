class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        lookup = set(nums)
        longest_sequence = 1
        for num in lookup:
            if num + 1 in lookup:
                curr = num
                curr_length = 1
                while curr + 1 in lookup:
                    curr_length += 1
                    curr += 1
                longest_sequence = max(longest_sequence, curr_length)
        
        return longest_sequence
