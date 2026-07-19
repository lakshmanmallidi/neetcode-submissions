class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(node, parent_val, max_v, min_v, relation):
            if node == None:
                return True
            if relation == "left":
                # Check: Current value must be smaller than the parent, but larger than the current minimum floor
                if node.val < parent_val and node.val > min_v:
                    # MINIMAL CHANGE HERE: Going left means this node becomes the new maximum ceiling for its children. 
                    # The floor (min_v) stays exactly what it was.
                    return traverse(node.left, node.val, node.val, min_v, "left") and \
                           traverse(node.right, node.val, max_v, node.val, "right")
                else:
                    return False
            else:
                # Check: Current value must be larger than the parent, but smaller than the current maximum ceiling
                if node.val > parent_val and node.val < max_v:
                    # MINIMAL CHANGE HERE: Going right means this node becomes the new minimum floor for its children. 
                    # The ceiling (max_v) stays exactly what it was.
                    return traverse(node.left, node.val, node.val, min_v, "left") and \
                           traverse(node.right, node.val, max_v, node.val, "right")
                else:
                    return False

        # MINIMAL CHANGE HERE: Initialize boundaries to infinity so the root doesn't get boxed in.
        return traverse(root, 1000, 1001, -1001, "left")