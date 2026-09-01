# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = [0]
        def dfs(root):
            if not root:
                return -1
            left = 1 + dfs(root.left)
            right = 1 + dfs(root.right)
            max_[0] = max(max_[0], left+right)
            return max(left, right)
        dfs(root)
        return max_[0]