# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    @staticmethod
    def print_list(head: Optional[ListNode]):
        while head != None:
            print(" ",head.val, end="")
            head = head.next
        print("")
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = (l1.val if l1 !=None else 0) + (l2.val if l2 !=None else 0)
        c = s//10
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
        out = ListNode(s%10)
        head = out
        while l1 != None and l2 != None:
            #Solution.print_list(head)
            s = c + l1.val + l2.val
            c = s//10
            out.next = ListNode(s%10)
            out = out.next
            l1 = l1.next
            l2 = l2.next

        while l1 != None:
            s = c + l1.val
            c = s//10
            out.next = ListNode(s%10)
            out = out.next
            l1 = l1.next
        
        while l2 != None:
            s = c + l2.val
            c = s//10
            out.next = ListNode(s%10)
            out = out.next
            l2 = l2.next
        
        if c != 0:
            out.next = ListNode(c)
        return head
        