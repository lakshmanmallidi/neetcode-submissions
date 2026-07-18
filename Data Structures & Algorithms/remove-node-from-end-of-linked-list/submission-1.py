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

    @staticmethod
    def print_list_till(head: Optional[ListNode], till: Optional[ListNode]):
        while head != None:
            print(" ",head.val, end="")
            if head==till:
                print("✓", end="")
            head = head.next
        print("")
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p2 = head
        p1 = head
        p0 = None
        i=0
        while i < n and p2 != None:
            p2 = p2.next
            i=i+1
        while p2 != None:
            p0 = p1
            p2 = p2.next
            p1 = p1.next
        if p0 != None:
            p0.next = p1.next
        else:
            head = p1.next
        #Solution.print_list_till(head, p2)
        #Solution.print_list_till(head, p1)
        #Solution.print_list_till(head, p0)
        
        return head