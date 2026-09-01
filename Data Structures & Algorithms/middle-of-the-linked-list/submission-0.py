# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp = {}
        i = 0
        while (head):
            temp[i]=head
            head = head.next
            i+=1
        middle = i // 2 
        return temp[middle]
        
