# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        riporto = 0
        dummy = ListNode(0)
        curr = dummy
        while l1:
            if not l2:
                val2 = 0
            else:
                val2 = l2.val
                l2 = l2.next
            val1 = l1.val
            res = val1 + val2 + riporto
            riporto = 0
            if res >= 10:
                riporto = 1
                res -= 10
            l1 = l1.next
            curr.next = ListNode(res)
            curr = curr.next
        while l2:
            if not l1:
                val1 = 0
            else:
                val1 = l1.val
                l1 = l1.next
            val2 = l2.val
            res = val1 + val2 + riporto
            riporto = 0
            if res >= 10:
                riporto = 1
                res -= 10
            l2 = l2.next
            curr.next = ListNode(res)
            curr = curr.next

        if riporto == 1:
            curr.next = ListNode(1)

        return dummy.next
            