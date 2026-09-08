# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p and q:
            return False
        elif not q and p:
            return False

        
        queue = deque([p])
        queue.append(q)
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()

            if node1.val != node2.val:
                return False
            if node1.left and node2.left:
                queue.append(node1.left)
                queue.append(node2.left)
            elif not node1.left and node2.left:
                return False
            elif node1.left and not node2.left:
                return False
            if node1.right and node2.right:
                queue.append(node1.right)
                queue.append(node2.right)
            elif not node1.right and node2.right:
                return False
            elif node1.right and not node2.right:
                return False

        return True

        
        