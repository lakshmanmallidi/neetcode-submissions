# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        g_prev = dummy
        while True:
            kth = g_prev.next
            c = 1
            while kth and c<k:
                kth = kth.next
                c = c+1
            if not kth:
                break
            #print("kth:", kth.val, kth.next.val)
            g_next = kth.next
            prev = kth.next 
            curr = g_prev.next
            while curr != g_next:
                #print("curr:", curr.val)
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = g_prev.next
            g_prev.next = kth
            g_prev = temp
        return dummy.next
