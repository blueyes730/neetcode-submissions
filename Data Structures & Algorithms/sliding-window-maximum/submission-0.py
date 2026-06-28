class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        l, r = 0, k-1
        for i in range(len(nums)-k+1):
            print(nums[i:i+(k)])
            subarray = nums[i:i+(k)]
            ret.append(max(subarray))

        return ret