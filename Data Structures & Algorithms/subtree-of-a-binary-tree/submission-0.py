# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self,root: Optional[TreeNode], subRoot: Optional[TreeNode])-> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if not subRoot and root:
            return False
        if root.val != subRoot.val:
            return False
        else:
            return self.isSametree(root.left,subRoot.left) and self.isSametree(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.isSametree(node,subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return False






        