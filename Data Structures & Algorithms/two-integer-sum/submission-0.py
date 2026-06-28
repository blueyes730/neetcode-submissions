class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        secondaries = dict()

        for i in range(len(nums)):
            secondary = target - nums[i]
            if secondary in secondaries:
                return [secondaries[secondary], i]
            else:
                secondaries[nums[i]] = i
        
        return [-1,-1]
        