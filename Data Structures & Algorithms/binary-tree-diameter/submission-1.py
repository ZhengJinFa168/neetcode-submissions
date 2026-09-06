# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self, root: Optional[TreeNode], diam) -> tuple:
        if not root:
            return (0, 0)  # (height, diameter) for an empty tree
        
        left_height, left_diam = self.depth(root.left, diam)
        right_height, right_diam = self.depth(root.right, diam)
        
        # Height of current node = 1 + max(left_height, right_height)
        current_height = 1 + max(left_height, right_height)
        
        # Diameter passing through this node = left_height + right_height
        current_diameter = max(diam, left_height + right_height, left_diam, right_diam)
    
        return (current_height, current_diameter)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.depth(root,0)[1]