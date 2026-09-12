# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        temp = []
        temp2 = head
        while temp2:
            temp.append(temp2)
            temp2 = temp2.next
        l = 0
        r = len(temp) - 1
        i = 0
        while l<r:
            node1 = temp[l]
            node2 = temp[r]
            temp1 = None
            if node1.next != node2:
                temp1 = node1.next
            node1.next = node2
            node2.next = temp1
            l += 1
            r -= 1
        temp[l].next = None

        return 


            
