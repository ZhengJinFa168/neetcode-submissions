# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        if not list1:
            head = list2
            return head
        elif not list2:
            head = list1
            return head

        if list1.val < list2.val:
            prev = ListNode(list1.val,None)
            list1 = list1.next
        else:
            prev = ListNode(list2.val,None)
            list2 = list2.next
        head = prev
        while list1 or list2:

            if not list1:
                prev.next = list2
                return head
            elif not list2:
                prev.next = list1
                return head

            if list1.val < list2.val:
                temp = ListNode(list1.val,None)
                list1 = list1.next
            else:
                temp = ListNode(list2.val,None)
                list2 = list2.next
            
            prev.next = temp
            prev = temp
            
        return head