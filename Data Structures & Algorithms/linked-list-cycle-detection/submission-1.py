# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=False
        while head!=None and visited != True:
            try:
                visited = head.visited
            except:
                head.visited = True
            head = head.next
        return visited