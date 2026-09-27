# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            len_q = len(queue)
            for i in range(len_q):
                node = queue.popleft()
                if node:
                    queue.append(node.right)
                    queue.append(node.left)
                    level.append(node.val)
            if level:
                res.append(level[0])

        return res

        