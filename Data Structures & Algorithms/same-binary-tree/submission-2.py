# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same_tree = [True]
        def dfs(p,q):
            if not (p and q):
                if p or q:
                    same_tree[0] = False
                    return
                else:
                    return
            if p.val != q.val:
                same_tree[0] = False
                return
            dfs(p.left, q.left)
            dfs(p.right, q.right)

        dfs(p,q)
        return same_tree[0]