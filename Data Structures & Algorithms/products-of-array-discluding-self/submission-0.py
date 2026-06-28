class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = []
        prefix = 1
        for i in range(len(nums)):
            ret.append(prefix)
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            ret[i] *= postfix
            postfix *= nums[i]

        return ret        
        