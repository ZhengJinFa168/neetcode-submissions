# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        h = 0
        queue.append([root,h])
        h += 1
        res = defaultdict(list)
        while queue:
            temp = queue.pop()
            node = temp[0]
            if node.right:
                queue.append([node.right,temp[1]+1])
            if node.left:
                queue.append([node.left,temp[1]+1])
            
            res[temp[1]].append(node.val)
        output=[]
        for k,v in res.items():
            output.append(v)
        return output