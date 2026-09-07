# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth (self,root : Optional[TreeNode]) -> [bool,int]:
        if not root:
            return [True,0]
        left = self.depth(root.left)
        right = self.depth(root.right)
        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
        return [balanced,max(left[1],right[1])+1]
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.depth(root)[0]
        