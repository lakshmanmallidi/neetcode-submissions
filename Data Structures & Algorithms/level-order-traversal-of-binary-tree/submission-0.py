# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.level_order = []
        def traverse(node, lvl):
            if node==None:
                return
            if len(self.level_order) < lvl:
                self.level_order.append([])
            self.level_order[lvl-1].append(node.val)
            traverse(node.left,1+lvl)
            traverse(node.right,1+lvl)
        
        traverse(root, 1)
        return self.level_order