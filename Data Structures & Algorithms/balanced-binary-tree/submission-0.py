# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.avl_tree = True
        def traverse(node):
            if node == None:
                return 0
            lh = traverse(node.left)
            rh = traverse(node.right)
            if abs(lh-rh) > 1:
                self.avl_tree = False
            return 1+max(lh, rh)
        traverse(root)
        return self.avl_tree