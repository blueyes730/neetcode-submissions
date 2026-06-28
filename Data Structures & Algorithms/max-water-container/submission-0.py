class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        
        max_area = 0
        while l < r:
            print(f"l = {l}, r = {r}")
            width = r-l
            cur_area = 0
            print(f"width = {width}")
            print(f"heights[{l}] = {heights[l]}, heights[{r}] = {heights[r]}")
            if heights[l] <= heights[r]:
                cur_area = (width)*heights[l]
                l += 1
            else:
                cur_area = (width)*heights[r]
                r -= 1
            print(f"cur_area = {cur_area}")
            max_area = max(cur_area, max_area)
            print(f"max_area = {max_area}")
        return max_area