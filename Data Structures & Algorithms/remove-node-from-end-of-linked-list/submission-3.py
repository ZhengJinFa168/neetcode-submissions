# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = []
        temp1 = head
        while temp1:
            node = temp1
            temp1 = temp1.next
            temp.append(node)
        sz = len(temp)
        if sz == 1:
            return None
        if sz == n:
            return head.next
        if n == 1:
            temp[sz - n - 1].next = None
            return head
        temp[sz - n - 1].next = temp[sz - n + 1]
        return head

        