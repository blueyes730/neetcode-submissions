class Solution:
    def trap(self, height: List[int]) -> int:
        # the area needed to be added is the 
        #   min between the max height on the right vs
        #   the max height of the left

        # if the max right side is taller than the max left,
        #   then the area at any moment is dependent
        #   on the max left height and vice versa

        # iterate from left while max left is less than right
        # iterate from right while max right is less than left
        
        # we should only take area measurement and add to total area
        #   when we go lower than the max
        # going to higher heights should not add any area
        
        total_area = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]

        while l <= r:
            # check which max to use
            print(f"total area: {total_area}")
            if max_l < max_r:
                # we will use the max left to find the area
                max_l = max(max_l, height[l])
                print(f"area found at {l}: {max_l - height[l]}" if max_l - height[l] > 0 else "at the same or increased elevation from the left")
                total_area += max_l - height[l] # if we increased in elevation, max_l = height[l]
                l += 1
            else:
                # we will use the max right to find the area
                max_r = max(max_r, height[r])
                print(f"area found at {r}: {max_r - height[r]}" if max_r - height[r] > 0 else "at the same or increased elevation from the right")
                total_area += max_r - height[r] # if we increased in elevation, max_r = height[r]
                r -= 1
            
        return total_area