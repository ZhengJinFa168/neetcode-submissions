# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        while list1 and list2:
            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
            else:
                temp.next = list1
                list1 = list1.next
            temp = temp.next
        
        temp.next = list1 or list2

        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 2:
            return self.mergeTwoLists(lists[0],lists[1])
        elif len(lists) == 1:
            return self.mergeTwoLists(lists[0],None)
        return self.mergeTwoLists(self.mergeKLists(lists[:len(lists)//2]),self.mergeKLists(lists[len(lists)//2:]))
        