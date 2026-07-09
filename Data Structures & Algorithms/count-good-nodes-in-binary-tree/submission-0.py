# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        stack = [(root, root.val)]
        while stack:
            curr, ref = stack.pop()
            if curr.val >= ref:
                good += 1
            
            ref = max(ref, curr.val)

            if curr.left:
                stack.append((curr.left, ref))
            if curr.right:
                stack.append((curr.right, ref))
        return good



