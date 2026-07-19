# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = deque()
        lvl_order = []
        def traverse():
            if len(queue)==0:
                return
            current = []
            nodes = []
            while queue:
                nodes.append(queue.popleft())
            for node in nodes:
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                current.append(node.val)
            print(current)
            lvl_order.append(current)
            traverse()
            
        queue.append(root)
        traverse()
        return lvl_order