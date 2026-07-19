# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def traverse(node, max_parent_val):
            if node == None:
                return 0
            if node.val >= max_parent_val:
                return 1+traverse(node.left, node.val)+traverse(node.right, node.val)
            else:
                return traverse(node.left, max_parent_val)+traverse(node.right, max_parent_val)

        return traverse(root, -1000)
        