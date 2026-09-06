# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self,root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.depth(root.left),self.depth(root.right)) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_right = self.depth(root.right)
        l_left = self.depth(root.left)
        diam = l_right + l_left
        temp = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return max(diam,temp)
        
        