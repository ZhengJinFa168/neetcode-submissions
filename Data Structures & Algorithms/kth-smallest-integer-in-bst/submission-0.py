# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sorted_array(self, root:TreeNode) -> List[int]:
        if not root:
            return []
        left = right = []
        if root.left:
            left = self.sorted_array(root.left)
        if root.right:
            right = self.sorted_array(root.right)
        return left+[root.val]+right
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = self.sorted_array(root)
        return sorted_array[k-1]
        

