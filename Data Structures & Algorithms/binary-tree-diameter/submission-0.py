# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def traverse(root):
            if root == None:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            if l+r > self.max_diameter:
                self.max_diameter = l+r
            return 1+max(l,r)
        traverse(root)
        return self.max_diameter