# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head != None:
            stack.append(head.val)
            head = head.next
        reverse_head = None
        if stack:
            reverse_head = ListNode()
            head = reverse_head
        while stack:
            head.val = stack.pop()
            if stack:
                head.next = ListNode()
                head = head.next
        return reverse_head