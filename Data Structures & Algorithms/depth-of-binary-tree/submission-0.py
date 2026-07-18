# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(root):
            if root == None:
                return 0
            l = 1+traverse(root.left)
            r = 1+traverse(root.right)

            return max(l,r)
        
        return traverse(root)