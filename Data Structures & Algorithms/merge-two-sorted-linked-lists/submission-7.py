# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        head = list3
        while list1 and list2:
            node = ListNode()
            if list1.val <= list2.val:
                node.val = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
            list3.next = node
            list3 = list3.next
        if list1:
            list3.next=list1
        else:
            list3.next=list2
        return head.next
