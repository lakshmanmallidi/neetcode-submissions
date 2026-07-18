# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.is_equal = True
        def traverse(p, q):
            if p==None or q==None:
                if not(p==None and q==None):
                    self.is_equal=False
                return 0
            if p.val != q.val:
                self.is_equal=False
            traverse(p.left, q.left)
            traverse(p.right, q.right)
        traverse(p,q)
        return self.is_equal