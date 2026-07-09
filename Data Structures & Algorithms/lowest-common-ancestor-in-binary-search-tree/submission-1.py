# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(root, p, q):    
            if root == None: return None
            if root.val == p.val or root.val == q.val: 
                print(root.val)
                return root
            left = search(root.left, p, q) 
            right = search(root.right, p, q)

            

            if left and not right: return left
            if right and not left: return right
            if left and right: return root
            return None        
        return search(root, p, q)