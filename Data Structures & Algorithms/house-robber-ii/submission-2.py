class Solution:
    def robber1(nums: List[int]) -> int:
        # either we rob first house and then third house, or we rob second hourse and move on.
        # we can keep track of max rewards by taking max of robbing (curr - 2 house plus curr house) or (curr - 1) house
        curr_min_2, curr_min_1 = 0,0

        for n in nums:
            temp = max(curr_min_2 + n, curr_min_1)
            curr_min_2 = curr_min_1 # we are moving one house to the right
            curr_min_1 = temp # max sum
        
        return curr_min_1
    def rob(self, nums: List[int]) -> int:
        return max(Solution.robber1(nums[1:]), Solution.robber1(nums[0:-1]), nums[0])