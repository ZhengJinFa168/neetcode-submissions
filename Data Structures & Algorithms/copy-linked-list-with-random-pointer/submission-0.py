"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        dummyHead = Node(0)
        new_temp = dummyHead
        hashmap = {}
        while temp:
            curr = Node (temp.val)
            new_temp.next=curr
            new_temp = new_temp.next
            hashmap[temp]=new_temp
            temp = temp.next
        
        temp = head
        new_temp = dummyHead.next
        while temp:
            pointer = hashmap.get(temp.random,None)
            new_temp.random = pointer
            temp = temp.next
            new_temp = new_temp.next

        return dummyHead.next
