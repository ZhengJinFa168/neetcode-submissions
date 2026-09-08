# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p,q)]
        while stack:
            node_left, node_right = stack.pop()
            if not node_left and not node_right:
                continue
            if not node_left and node_right:
                return False
            if node_left and not node_right:
                return False
            if node_left.val != node_right.val:
                return False
            
            stack.append((node_left.left,node_right.left))
            stack.append((node_left.right,node_right.right))

        return True