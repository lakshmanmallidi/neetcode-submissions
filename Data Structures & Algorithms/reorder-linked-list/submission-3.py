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

    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        prev = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        #Solution.print_list_till(head, slow)
        #Solution.print_list_till(head, prev_slow)
        prev.next = None
        #Solution.print_list(head)
        prev = None
        while slow != None:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        temp = None
        while prev!=None and head!=None:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            head=temp1
            temp = prev
            prev=temp2
        if prev != None:
            temp.next = prev
 