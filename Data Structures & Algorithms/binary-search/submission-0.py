class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            med = (r+l)//2
            if nums[med] > target:
                r = med - 1
            elif nums[med] < target:
                l = med + 1
            else: return med
        return -1