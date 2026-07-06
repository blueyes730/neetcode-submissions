# [7,8,0,1,2,3,4,5,6]

# mid = 8 + 0 // 2 = 4
# nums[mid] = nums[4] = 2


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums) - 1

        if nums[l] < nums[r]: return nums[l]

        reference = nums[0]
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < reference:
                r = mid - 1
            else: l = mid + 1

