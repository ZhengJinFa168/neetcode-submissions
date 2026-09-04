# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        flag = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                flag = 1
                temp = node.left
            if node.right:
                queue.append(node.right)
                if flag == 1:
                    flag = 3
                else:
                    flag = 2
            if flag == 1:
                node.right = node.left
                node.left = None
            elif flag == 2:
                node.left = node.right
                node.right = None
            elif flag == 3:
                temp = node.left
                node.left = node.right
                node.right = temp
        return root

