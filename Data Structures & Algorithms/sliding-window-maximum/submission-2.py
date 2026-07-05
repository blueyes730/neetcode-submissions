class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # get intial max
        # every iteration, check if max val is leaving
        # if max_val hasnt left, compare max val with new val
        # if max val left, 
        # output = []
        # max_val = max(nums[0: k]) 
        # for l in range(0, len(nums) - k + 1, 1):
        #     r = l + k - 1
        return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]
            
