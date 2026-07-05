class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # height of rectangle depends on smaller of the two sides
        # rectangle height depends on the current height and all contiguous neighboring heights with height >= curr_height
        # if we are at rect[i] and rect[i+1] is smaller, then we know we cannot continue the existing rectangle
        # at rect[i], if we look at the lastly processed rect, if last rect height > curr rect height, curr rect height
        # if curr height is greater than last height, we add to last height rect
        # if curr height is less than last rct height, that rect is done and pop from stack
        # add recent rect to stack, pop when rect is done
        # add to stack when height is greater than or equal to, add [height, l, r + 1] or [height, width + 1]
        # if rect of hieght < stack.top() rect, pop stack, take max between curr max and that rect area, then change height to new height and increase width

        stack = [-1] # if we are at height[i], and we pop, and there are no heights shorter than ith, then we ne assume that we can make a rectanlge of height[i] with width all the way to the start

        max_area = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                curr = stack.pop()
                curr_height = heights[curr]
                curr_width = i - 1 - stack[-1] # i is right bound non inclusive, so i - 1, stack[-1] is left bound where a valid left bound is a height that is greater that the curr height
                # essentially we pop when the right bound becomes invalid and stop when the left bound becomes invalid
                max_area = max(max_area, curr_height * curr_width)
            stack.append(i)


        # handle left overs

        while stack[-1] != -1:
            curr = stack.pop()
            curr_height = heights[curr]
            curr_width = len(heights) - 1 - stack[-1]
            max_area = max(max_area, curr_height * curr_width)
        return max_area 

