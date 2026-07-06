class Solution:
    def search(self, nums: List[int], target: int) -> int:
        reference = nums[0]
        rotated = True
        right = True if target < reference else False
        if nums[0] < nums[-1]: rotated = False
        l, r = 0, len(nums) - 1


        while l <= r:
            mid = l + ((r - l)//2) # int overflow safe
            midval = nums[mid]
            print(f"l: {l}, r: {r}, mid: {mid}, midval: {midval}")
            if midval == target:
                return mid
            
            if rotated:
                if midval >= reference:
                    #left side
                    if right:
                        l = mid + 1
                    else:
                        if midval > target:
                            r = mid - 1
                        else:
                            l = mid + 1
                else:
                    # right side
                    if right:
                        if midval > target:
                            r = mid - 1
                        else:
                            l = mid + 1
                    else:
                        r = mid - 1
            else:
                if midval > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1