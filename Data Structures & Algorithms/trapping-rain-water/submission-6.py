class Solution:
    def trap(self, height: List[int]) -> int:
    # find first l that does not have 0 height
        if not height:
            return 0

        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]

        area = 0

        while l < r:
            if lmax < rmax:
                l += 1
                lmax = max(lmax, height[l])
                area += lmax - height[l]

            else:
                r -= 1
                rmax = max(rmax, height[r])
                area += rmax - height[r]
        return area
        

